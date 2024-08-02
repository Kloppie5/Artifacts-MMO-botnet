
class Action {

    start() {}

}

class RepeatedAction extends Action {

    constructor(count, action){
        this.count = count;
        this.action = action;
    }

    start(){
        for(let i = 0; i < times; i++){
            this.action.start();
        }
    }
}

class MoveAction extends Action {
    
}

class GatheringAction extends Action {

}