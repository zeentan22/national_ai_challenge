from sgnlp.models.sentic_gcn.train import SenticGCNTrainer, SenticGCNBertTrainer
from sgnlp.models.sentic_gcn.utils import parse_args_and_load_config, set_random_seed


cfg = parse_args_and_load_config("/Users/zeen22/Documents/national_ai_challenge/config/sentic_gcn_bert_config.json")
if cfg.seed is not None:
    set_random_seed(cfg.seed)
trainer = SenticGCNTrainer(cfg) if cfg.model == "senticgcn" else SenticGCNBertTrainer(cfg)
trainer.train()


