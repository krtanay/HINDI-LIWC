# Hindi LIWC Package

This folder contains an initial structure for the Hindi LIWC (Linguistic Inquiry and Word Count) package.

The project aims to develop a psycholinguistic lexicon and toolkit for Hindi, following the steps outlined previously:

1. **Define the theoretical framework:** Establish categories for affect, cognition, social processes, drives, etc., and adapt them for Hindi culture.
2. **Construct a representative corpus:** Collect and preprocess Hindi texts across multiple domains, including Romanized and code-mixed samples.
3. **Create a seed lexicon:** Translate and adapt the English LIWC categories using bilingual experts, Hindi WordNet, and cross‑lingual embeddings.
4. **Normalize morphology:** Apply lemmatization/stemming and handle inflectional variants.
5. **Validate via embeddings:** Use contextual embeddings (e.g., IndicBERT) to cluster and validate category assignments.
6. **Calibrate context:** Annotate a sample corpus and train models to auto‑expand and refine categories.
7. **Handle Romanization:** Include transliteration to support Romanized Hindi.
8. **Cross‑validate and test reliability:** Compare category usage across translated corpora and compute reliability metrics.
9. **Build the software toolkit:** Provide a Python API for text analysis.

This repository contains placeholder code and documentation to start the implementation. Further contributions should add actual lexicons, preprocessing code, and machine learning components.