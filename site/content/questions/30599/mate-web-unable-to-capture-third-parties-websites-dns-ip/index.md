+++
type = "question"
title = "MATE web unable to capture third parties websites DNS IP"
description = '''I have been using the configurantion file(web.mate) below to try and capture the DNS ip from the third parties web sites but unfortunelly no sucess. The configuration file works fine but i am only getting my router IP and my machine ip. Can someone shed some light to my torment or even provide me wi...'''
date = "2014-03-08T05:47:00Z"
lastmod = "2014-03-09T11:42:00Z"
weight = 30599
keywords = [ "parties", "dns", "websites", "third", "gop" ]
aliases = [ "/questions/30599" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [MATE web unable to capture third parties websites DNS IP](/questions/30599/mate-web-unable-to-capture-third-parties-websites-dns-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30599-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have been using the configurantion file(web.mate) below to try and capture the DNS ip from the third parties web sites but unfortunelly no sucess. The configuration file works fine but i am only getting my router IP and my machine ip. Can someone shed some light to my torment or even provide me with a hint where i am going wrong??? Many Thanks Felgueiras</p><pre><code>Pdu tcp_pdu Proto tcp Transport ip {
    Extract addr From ip.addr;
    Extract port From tcp.port;
    Extract tcp_start From tcp.flags.syn;
    Extract tcp_stop From tcp.flags.reset;
    Extract tcp_stop From tcp.flags.fin;
};

Gop tcp_ses On tcp_pdu Match (addr, addr, port, port) {
    Start (tcp_start=1);
    Stop (tcp_stop=1);
};

Transform rm_client_from_dns_resp {
    Match (dns_resp=1, client) Insert (dns_resp=1); 
};

Pdu dns_pdu Proto dns Transport ip {
    Extract addr From ip.addr;
    Extract dns_resp From dns.flags.response;
    Extract host From dns.qry.name;
    Extract client From ip.src;
    Extract dns_id From dns.id;
    Transform rm_client_from_dns_resp;

};

Transform rm_client_from_http_resp1 {
    Match (http_rq);
    Match (addr) Insert (not_rq);
    Match (not_rq,client);
};

Transform rm_client_from_http_resp2 {
    Match (not_rq,client);
};

Pdu http_pdu Proto http Transport tcp/ip {
    Extract addr From ip.addr;
    Extract port From tcp.port;
    Extract http_rq From http.request.method;
    Extract http_rs From http.response;
    Extract host From http.host;
    Extract client From ip.src;
    Transform rm_client_from_http_resp1;
//  Transform rm_client_from_http_resp2;

};

Gop dns_req On dns_pdu Match (addr, addr, dns_id) {
    Start (dns_resp=0);
    Stop (dns_resp=1);
    Extra (host, client);
};

Gop http_req On http_pdu Match (addr, addr, port, port) {
    Start (http_rq);
    Stop (http_rq);
    Extra (host, client);
};
</code></pre></div><div id="question-tags" class="tags-container tags">parties dns websites third gop</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Mar '14, 05:47</strong></p><img src="https://secure.gravatar.com/avatar/0a3b4fbdc2dd9a1df2ab73cc8e78d925?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Astrokilla23&#39;s gravatar image" /><p>Astrokilla23<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Astrokilla23 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Mar '14, 03:23</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-30599" class="comments-container"><span id="30608"></span><div id="comment-30608" class="comment"><div id="post-30608-score" class="comment-score"></div><div class="comment-text"><p>what exactly do you mean by: "the <strong>DNS ip</strong> from the third parties web sites"?</p><p>Isn't the destination IP address of the conversation, the address of the web site?</p></div><div id="comment-30608-info" class="comment-info"><span class="comment-age">(09 Mar '14, 03:24)</span> Kurt Knochner ♦</div></div><span id="30616"></span><div id="comment-30616" class="comment"><div id="post-30616-score" class="comment-score"></div><div class="comment-text"><p>Thanks for replaying to my question Kurt .What i trying to explain is that the source ip and destination ip are almost same(there's only two ip in which changes to source and destination)!!!So if i am on a web page and then a click on the add banner(Third party web site)i should be able to get the ip o source of the add() is coming from ???</p></div><div id="comment-30616-info" class="comment-info"><span class="comment-age">(09 Mar '14, 05:32)</span> Astrokilla23</div></div></div><div id="comment-tools-30599" class="comment-tools"></div><div class="clear"></div><div id="comment-30599-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30620"></span>

<div id="answer-container-30620" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30620-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>So <strong>if i am on a web page</strong> and then a <strong>click on the add banner</strong>(Third party web site)i <strong>should be able to get the ip</strong> of source of the add() is coming from ?</p></blockquote><p>I don't think that MATE can do that, as the page that get's loaded is totally unrelated to the previous TCP connection. The only 'link' between those two connections is the link in the HTML code of the web page transmitted in the first tcp connection.</p><p>So, you would have to</p><ul><li>parse the HTML code</li><li>figure out that there are several links</li><li>remember all host names of those links</li><li>look for DNS requests to those names</li><li>look for new tcp connections to the IP address of one of those host names</li></ul><p>AFIAK, there is no way to do that with MATE, especially because of the HTML parsing part!</p><p>Can you describe what you are trying to do? Maybe there is another solution.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Mar '14, 11:42</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Mar '14, 11:43</p></div></div><div id="comments-container-30620" class="comments-container"><span id="30664"></span><div id="comment-30664" class="comment"><div id="post-30664-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt thanks once again to take your time to answer my queries. I am doing a project on wireshark, called "Visualization of Third-Party websites" using Wireshark.I was instructed to use MATE because it can create group of protocols.By using mate i thought that i could create a gop of DNS's IP's and consequently use GEO IP to display their location on the map.I hope this gives you an insight of what i am trying to achieve.Can you please help me to get aroud this issue ?? Thanks Astrokilla.</p></div><div id="comment-30664-info" class="comment-info"><span class="comment-age">(10 Mar '14, 13:15)</span> Astrokilla23</div></div><span id="30665"></span><div id="comment-30665" class="comment"><div id="post-30665-score" class="comment-score"></div><div class="comment-text"><p>I'm not quite sure what you are trying to do. Do you want to visualize 'nested' content in web pages, by geoip mapping the addresses of the hostnames in those 'nested' links? If so, I'm pretty sure you can't do that with MATE (see my explanation above), so there is no (simple) way around this 'issue'.</p></div><div id="comment-30665-info" class="comment-info"><span class="comment-age">(10 Mar '14, 15:37)</span> Kurt Knochner ♦</div></div><span id="30667"></span><div id="comment-30667" class="comment"><div id="post-30667-score" class="comment-score"></div><div class="comment-text"><p>Well the visualization bit i can use any ip tracker website i am mostly interested in capturing the IP's and consequently track them if thats fine....</p></div><div id="comment-30667-info" class="comment-info"><span class="comment-age">(10 Mar '14, 16:12)</span> Astrokilla23</div></div></div><div id="comment-tools-30620" class="comment-tools"></div><div class="clear"></div><div id="comment-30620-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

