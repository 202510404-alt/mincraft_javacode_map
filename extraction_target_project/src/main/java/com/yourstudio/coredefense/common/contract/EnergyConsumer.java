package com.yourstudio.coredefense.common.contract;

public interface EnergyConsumer {
    int getEnergyDemand();
    void onEnergyAllocated(int amount);
}
