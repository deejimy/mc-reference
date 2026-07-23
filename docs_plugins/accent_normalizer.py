import unicodedata
import json
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options

class AccentNormalizerPlugin(BasePlugin):
    """Plugin to normalize accents in MkDocs search"""
    
    config_scheme = (
        ('enabled', config_options.Type(bool, default=True)),
    )
    
    def remove_accents(self, text):
        """Remove accents from text"""
        if not isinstance(text, str):
            return text
        nfkd = unicodedata.normalize('NFKD', text)
        return ''.join([c for c in nfkd if not unicodedata.combining(c)])
    
    def on_post_build(self, config):
        """Add normalized versions to the search index"""
        if not self.config['enabled']:
            return
        
        try:
            search_index_path = config['site_dir'] + '/search/search_index.json'
            
            with open(search_index_path, 'r', encoding='utf-8') as f:
                search_data = json.load(f)
            
            # For each document, create a normalized version
            new_docs = []
            for doc in search_data.get('docs', []):
                # Keep the original
                new_docs.append(doc)
                
                # Create a normalized version
                normalized_doc = doc.copy()
                normalized_doc['title'] = self.remove_accents(doc.get('title', ''))
                normalized_doc['text'] = self.remove_accents(doc.get('text', ''))
                normalized_doc['location'] = self.remove_accents(doc.get('location', ''))
                
                new_docs.append(normalized_doc)
            
            search_data['docs'] = new_docs
            
            with open(search_index_path, 'w', encoding='utf-8') as f:
                json.dump(search_data, f, ensure_ascii=False, indent=2)
            
            print(f"✓ {len(new_docs)} index entries (originals + normalized)")
        
        except FileNotFoundError:
            print("⚠ Search index file not found")
        except Exception as e:
            print(f"✗ Error: {e}")