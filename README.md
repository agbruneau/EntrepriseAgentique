# Architecte d'Interopérabilité Cognitive (AIC)

Ce dépôt contient la base de connaissances et la définition fondamentale de l'**Architecte d'Interopérabilité Cognitive (AIC)**, un agent IA spécialisé dans l'architecture d'entreprise.

## Mission

La mission de l'AIC est de fournir des analyses architecturales, des recommandations stratégiques et des solutions techniques en synthétisant deux domaines de connaissance :

1.  **Les Patrons d'Intégration d'Entreprise (EIP)** : Les solutions tactiques et éprouvées pour l'intégration de systèmes.
2.  **L'Entreprise Agentique** : Une vision stratégique pour la construction d'organisations adaptatives basées sur des agents autonomes.

L'agent est conçu pour ne jamais dissocier la solution technique de la vision stratégique, assurant ainsi que chaque recommandation est à la fois pragmatique et visionnaire.

## Composants du Dépôt

Ce dépôt est structuré autour de deux types de composants : le Méta-Prompt, qui définit l'agent, et la Base de Connaissances, qui alimente son expertise.

### 1. Méta-Prompt

Le fichier `MetaPrompt.txt` est le document central de ce projet. Il agit comme la "constitution" ou le "système d'exploitation" de l'agent AIC. Il définit :
- **L'Identité et la Mission** : Qui est l'agent et quel est son but.
- **Le Moteur de Raisonnement (Framework PERFECT)** : Un processus interne en plusieurs étapes (Préparation, Ébauche, Raffinement, Finalisation, Correction, Thésaurisation) que l'agent doit suivre pour garantir la qualité et la rigueur de ses analyses.
- **Le Format de Sortie Strict** : Une structure de réponse en quatre parties (Analyse, Fondations Tactiques, Perspective Stratégique, Recommandation) que chaque réponse de l'agent doit respecter.

### 2. Base de Connaissances (Corpus Documentaire)

Les documents PDF constituent la source de connaissances exclusive sur laquelle l'agent s'appuie. Ils sont organisés comme suit :

#### Socle Tactique
- **`0 - EIP - Enterprise Integration Patterns.pdf`**: Fournit le vocabulaire, les patrons de conception et les solutions techniques pour les systèmes de messagerie. Il s'agit de l'ouvrage de référence de Gregor Hohpe et Bobby Woolf.
- **`6 - Kafka - Data Streaming.pdf`**: Document complémentaire sur les technologies de streaming de données.
- **`7 - Confluent - Guide de Design des systèmes multi-agents.pdf`**: Document complémentaire sur la conception de systèmes multi-agents.


#### Cadre Stratégique ("La Monographie Agentique")
- **`1 - Plan Directeur – Architecture d’Interopérabilité Agentique.pdf`**: Introduit la vision de l'Entreprise Agentique et l'interopérabilité cognitivo-adaptative.
- **`2 - Ingénierie Systémique – Architecture et Orchestration Maillage Agentique et AgentOps.pdf`**: Détaille l'architecture du Maillage Agentique et la discipline AgentOps pour la gouvernance.
- **`3 - Chorégraphie Stigmergie - Coordination et Médiation Algorithmiques Agentiques.pdf`**: Explore les algorithmes de coordination et de négociation décentralisée pour les agents.
- **`4 - Entreprise Agentique - Livre Blanc.pdf`**: Livre blanc sur l'entreprise agentique.
- **`5 - Entreprise Agentique - Réinventer Entreprise avec Agents Autonomes.pdf`**: Document complémentaire sur la réinvention de l'entreprise avec des agents autonomes.


## Utilisation

Ce dépôt sert de référence pour comprendre le fonctionnement interne de l'agent AIC. Le `MetaPrompt.txt` peut être utilisé pour instancier un agent Large Language Model (LLM) avec les capacités décrites, tandis que les PDF servent de corpus pour un système de Retrieval-Augmented Generation (RAG).
