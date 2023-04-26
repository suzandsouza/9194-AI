import java.util.*;

public class ucs {
    static class Node implements Comparable<Node> {
        int[] state;  // current state
        Node parent;  // parent node
        int depth;  // depth of the node in the search tree
        int cost;  // cost of the path from the initial state to the current state

        public Node(int[] state, Node parent, int depth, int cost) {
            this.state = state;
            this.parent = parent;
            this.depth = depth;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node o) {
            return this.cost - o.cost;
            //current cost-original cost
        }
    }

    // check if a state is a valid state
    static boolean isValid(int[] state) {
        int m = state[0];
        int c = state[1];
        int b = state[2];
        return (m >= 0 && c >= 0 && b >= 0 && (m == 0 || m >= c) && (m == 3 || m >= 3 - c));
    }

    // check if a state is the goal state
    static boolean isGoal(int[] state) {
        return state[0] == 0 && state[1] == 0 && state[2] == 0;
    }

    // find the next possible states from a given state
    static List<Node> expand(Node node) {
        List<Node> nextStates = new ArrayList<>();
        int[][] moves = {{2, 0, 1}, {1, 1, 1}, {0, 2, 1}, {1, 0, 1}, {0, 1, 1}};
        int m = node.state[0];
        int c = node.state[1];
        int b = node.state[2];
        for (int[] move : moves) {
            int[] nextState = {m - move[0], c - move[1], b - move[2]};
            if (isValid(nextState)) {
                nextStates.add(new Node(nextState, node, node.depth + 1, node.cost + move[2]));
            }
        }
        return nextStates;
    }

    public static void main(String[] args) {
        int[] initialState = {3, 3, 1};
        int[] goalState = {0, 0, 0};
        PriorityQueue<Node> frontier = new PriorityQueue<>();
        Set<String> explored = new HashSet<>();
        Node initialNode = new Node(initialState, null, 0, 0);
        frontier.add(initialNode);
        while (!frontier.isEmpty()) {
            Node node = frontier.poll();
            if (isGoal(node.state)) {
                // trace the path from the initial state to the goal state
                List<int[]> path = new ArrayList<>();
                while (node != null) {
                    path.add(node.state);
                    node = node.parent;
                }
                Collections.reverse(path);
                for (int[] state : path) {
                    System.out.println(Arrays.toString(state));
                }
                break;
            }
            explored.add(Arrays.toString(node.state));
            List<Node> nextStates = expand(node);
            for (Node nextState : nextStates) {
                if (!explored.contains(Arrays.toString(nextState.state))) {
                    frontier.add(nextState);
                }
            }
        }
    }
}
