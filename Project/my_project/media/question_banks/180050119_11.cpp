#include<bits/stdc++.h>

using namespace std;

typedef list<string>::iterator itr;
typedef unordered_map<string,itr>::iterator itr_m;
typedef long long int ll;
vector<pair<int,int> > parent_nd_cap;
vector<list<string> > recent_string_lst;
vector<unordered_map<string,itr> > vec_maps;
vector<ll> node_cost;
ll total_cost;

void search_query(string st,int num){
	itr_m it = vec_maps[num].find(st);
	total_cost+=node_cost[num];
	if(num==0){
		//total_cost+=node_cost[0];
		return;
	}
	else{
		if(it==vec_maps[num].end()){
			//total_cost+=parent_nd_cap[num].second;
			if(vec_maps[num].size()==parent_nd_cap[num].second){
				string s = *(recent_string_lst[num].begin());
				recent_string_lst[num].pop_front();
				recent_string_lst[num].push_back(st);
				vec_maps[num].erase(s);
				itr temp_itr=recent_string_lst[num].end();
				temp_itr--;
				vec_maps[num].insert({st,temp_itr});
			}
			else{
				recent_string_lst[num].push_back(st);
				itr temp_itr=recent_string_lst[num].end();
				temp_itr--;
				vec_maps[num].insert({st,temp_itr});		
			}
			search_query(st,parent_nd_cap[num].first);
		}
		else{
			//total_cost+=parent_nd_cap[num].second;
			itr it_instring= it->second;
			recent_string_lst[num].erase(it_instring);
			recent_string_lst[num].push_back(st);
			itr temp_itr=recent_string_lst[num].end();
			temp_itr--;
			vec_maps[num].insert({st,temp_itr});
			return;
		}
	}
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n,m;
	cin>>n>>m;
	int x;
	parent_nd_cap.resize(n);
	recent_string_lst.resize(n);
	vec_maps.resize(n);
	node_cost.resize(n);
	parent_nd_cap[0].first=-1;
	parent_nd_cap[0].second=m;
	total_cost=0;
	
	for(int i=1;i<n;i++){
		cin>>x;
		parent_nd_cap[i].first=x;
	}
	node_cost[0]=1+ll(log2(m));
	for(int i=1;i<n;i++){
		cin>>x;
		parent_nd_cap[i].second=x;
		node_cost[i]=1+ll(log2(x));
	}

	string str;
	int node_num;
	int k=m;
	while(k>0){
		cin>>str>>node_num;
		search_query(str,node_num);
		k--;
	}

	cout<<total_cost<<endl;
}