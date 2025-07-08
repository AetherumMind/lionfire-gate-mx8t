def launch_genesis_system():
    from avatar.character import build_avatar
    from tree_of_life.structure import initialize_hierarchy
    from tree_of_life.command_chain import activate_chain
    from tree_of_life.portal import open_portal
    print("\n🌿 Launching Genesis System...")
    build_avatar()
    initialize_hierarchy()
    activate_chain()
    open_portal()

if __name__ == "__main__":
    launch_genesis_system()