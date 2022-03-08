# FedBFT
Federated learning, blockchain and data asset

go get github.com/rimiti/kill-port
# Use protobuf to serialize data and use g-RPC to communciate with Peer Privacy Verification    
```
cd ~/fedbft/voting
go build .
protoc --go_out=. --go_opt=paths=source_relative \
    --go-grpc_out=. --go-grpc_opt=paths=source_relative \
    p4p/p4p/sim/p4p/p4p.proto
    
    
protoc --go_out=. --go_opt=paths=source_relative \
    --go-grpc_out=. --go-grpc_opt=paths=source_relative \
    p4p/p4p/user/p4p/users.proto
    
protoc --go_out=. --go_opt=paths=source_relative \
    --go-grpc_out=. --go-grpc_opt=paths=source_relative \
    p4p/p4p/userserver/p4p/userserver.proto
    
protoc --go_out=. --go_opt=paths=source_relative \
    --go-grpc_out=. --go-grpc_opt=paths=source_relative \
    p4p/p4p/userpeer/p4p/userpeer.proto
    
    
cp -r  ~/grpc-go/examples/p4p  ~/go/src/google.golang.org/grpc/examples/

# go run ~/grpc-go/examples/p4p/p4p/sim/server/server.go   
```  
