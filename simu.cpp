#pragma GCC optimize ("-O2")
#include <bits/stdc++.h>
using namespace std;
#define fastio ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define all(x) x.begin(),x.end()
#define memreset(a) memset(a,0,sizeof(a))
#define testcase(t) int t;cin>>t;while(t--)
#define forstl(i,v) for(auto &i: v)
#define forn(i,e) for(int i = 0; i < e;++i)
#define forsn(i,s,e) for(int i = s; i < e;++i)
#define rforn(i,s) for(int i = s; i >= 0;--i)
#define rforsn(i,s,e) for(int i = s; i >= e;--i)
#define bitcount(a) __builtin_popcount(a) // set bits (add ll)
#define ln '\n'
#define getcurrtime ((double)clock()/CLOCKS_PER_SEC)
#define dbgarr(v,s,e) cerr<<#v<<" = "; forsn(i,s,e) cerr<<v[i]<<", "; cerr<<endl
#define inputfile freopen("input.txt", "r", stdin)
#define outputfile freopen("output.txt", "w", stdout)
#define dbg(args...) { string _s = #args; replace(_s.begin(), _s.end(), ',', ' '); \
stringstream _ss(_s); istream_iterator<string> _it(_ss); err(_it, args); }
void err(istream_iterator<string> it) { cerr<<endl; }
template<typename T, typename... Args>
void err(istream_iterator<string> it, T a, Args... args) {
    cerr << *it << " = " << a << "\t"; err(++it, args...);
}
template<typename T1,typename T2>
ostream& operator <<(ostream& c,pair<T1,T2> &v){
    c<<"("<<v.fi<<","<<v.se<<")"; return c;
}
template <template <class...> class TT, class ...T>
ostream& operator<<(ostream& out,TT<T...>& c){
    out<<"{ ";
    forstl(x,c) out<<x<<" ";
    out<<"}"; return out;
}

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<ll,ll> p64;
typedef pair<int,int> p32;
typedef pair<int,p32> p96;
typedef vector<ll> v64;
typedef vector<int> v32; 
typedef vector<v32> vv32;
typedef vector<v64> vv64;
typedef vector<p32> vp32;
typedef vector<p64> vp64;
typedef vector<vp32> vvp32;
typedef map<int,int> m32;

const int LIM=1e5+5, MOD=1e9+7;
const ld EPS = 1e-9;

// The above is simply a template to make coding easier. 


signed main(){
    fastio;

    // Concept: A simple implementation has been created to simulate a part of the Jupyter architecture.
    // There are 8 ToRs and 4 switches. Each ToR is connected to each switch, and ToRs are communicating with each other.
    // We have simulated this process and calculated probability of blocking in this case. The answer turns out to be 
    // very close to ideal. 

    mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

    // A random generator based on the current clock time. This helps create truly random seeds and produce a distribution
    // That is closer to the ideal

    unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
    std::default_random_engine generator (seed);

    forsn(i,1,10000){
        
        // We are simulating the whole process at different arrival rates, according to which lambda changes (mean of poisson)

        std::poisson_distribution<int> distribution(i*0.0001);
        
        
        queue<pair<int,p32> > buffer[12], nodebuf[32];

        // NOTE: The switches are numbered 9-12 and the ToRs are numbered 1-8

        // the buffer stores upto 5 values for each of the 4 switches in the aggregation block
        // similarly for the nodebuf, which only stores values for the ToRs
        // in nodebuf, if a ToR has to send data to switch x, then the index chosen is (x-8)*4+ToR_index
        // This is because there is a seperate line from each ToR to switch

        int time1[12] = {0};
        
        // time1 denotes time remaining for the switch to receive data

        int time2[12] = {0};

        // time2 denotes the time remaining for the switch to send data

        int tp[8*4] = {0};

        // tp stores the time pending for each of the nodes, per link. If switch is x and ToR number is y, then index is
        // (x-8)*4+y, same as before

        pair<int,p32> curr[12];

        // curr stores the information about the data that is currently being processed by the switch, in the format
        // amount of data/ sender node/ receiver node

        ld a=0;
        ld b=0;

        // a and b are variables used to denote the sum of blocking across all times, from which we can get blocking probability,
        // and checking whether poisson distribution is close to ideal

        ll NoOfIterations = 10000;

        // The No of seconds for which we are simulating the process - it is a discrete event simulation

        forn(i,NoOfIterations){


            int blocking=0;

            // Assume that no node is blocking at the start. We will increment this variable as needed

            forsn(j,8,12){

                // Going through all the switches and updating their states

                if(time1[j]>0){
                    time1[j]--;
                    tp[(j-8)*4+curr[j].se.fi]--;
                    // time1[curr[j].se.fi]--;
                    if(time1[j]==0){
                        time2[j] = curr[j].fi;
                        tp[(j-8)*4+curr[j].se.se] = curr[j].fi;
                    }

                }

                else if(time2[j]>0){
                    time2[j]--;
                    time2[(j-8)*4+curr[j].se.fi]--;
                    if(time2[j]==0){
                        if(buffer[j].size()!=0){
                            curr[j] = buffer[j].front();
                            buffer[j].pop();
                            time1[j] = curr[j].fi;
                            tp[(j-8)*4+curr[j].se.fi] = curr[j].fi;
                        }
                    }
                }
                else{
                    if(buffer[j].size()!=0){
                        curr[j] = buffer[j].front();
                        buffer[j].pop();
                        time1[j] = curr[j].fi;
                        tp[(j-8)*4+curr[j].se.fi] = curr[j].fi;
                    }
                }
            }

            forn(j,8){

                // Going through all the ToRs and updating their states

                int z = distribution(generator);

                // this is sampling a poisson distribution

                b+=z;

                // b is a variable used to check ideality of the distribution - if mean is close to the expected.

                
                int destport = rng()%8;
                // Random numbers have been generated for the destination port 
                int agg = rng()%4;

                if(tp[agg*4+j]!=0){

                    // meaning that this line is not free currently

                    if(nodebuf[agg*4+j].size()<5){

                        // We are storing in the buffer at current node
                        if(z>0) nodebuf[agg*4+j].push(mp(z,mp(j,destport)));
                    }

                    else{
                        // We are dropping the packet if it is of non zero size
                        if(z>0) blocking++;
                    }

                }
                else{

                    if(nodebuf[agg*4+j].size()>0){

                        // Checking if buffer is empty

                        pair<int,p32> temp = nodebuf[agg*4+j].front();
                        nodebuf[agg*4+j].pop();
                        if(z>0) nodebuf[agg*4+j].push(mp(z,mp(j,destport)));
                        if(buffer[agg+8].size()<5) buffer[agg+8].push(temp);
                        else blocking++;
                    }

                    else if(buffer[8+agg].size()<5 && z>0) buffer[8+agg].push(mp(z,mp(j,destport)));
                    
                    else if(z>0) blocking++;
                }
            }
            a+=blocking;
        }
        
        cout<<setprecision(10)<<fixed;  
        // cout<<b/(8*NoOfIterations)<<ln;
        cout<<i*0.0001<<" "<<a/NoOfIterations<<ln;
    }

    return 0;
}