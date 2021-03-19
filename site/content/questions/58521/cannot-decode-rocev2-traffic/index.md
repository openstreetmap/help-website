+++
type = "question"
title = "Cannot decode ROCEv2 traffic"
description = '''Hi I am using 2.3.0 (tried 2.2.3 also) and feeding it a capture file containing ROCEv2 traffic. But it is not able to decode those packets. Any idea how to do the same ? Thanks Sumit'''
date = "2017-01-04T18:20:00Z"
lastmod = "2017-01-07T10:46:00Z"
weight = 58521
keywords = [ "rdma", "rocev2" ]
aliases = [ "/questions/58521" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot decode ROCEv2 traffic](/questions/58521/cannot-decode-rocev2-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58521-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58521-score" class="post-score" title="current number of votes">0</div><span id="post-58521-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I am using 2.3.0 (tried 2.2.3 also) and feeding it a capture file containing ROCEv2 traffic. But it is not able to decode those packets. Any idea how to do the same ?</p><p>Thanks Sumit</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rdma" rel="tag" title="see questions tagged &#39;rdma&#39;">rdma</span> <span class="post-tag tag-link-rocev2" rel="tag" title="see questions tagged &#39;rocev2&#39;">rocev2</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jan '17, 18:20</strong></p><img src="https://secure.gravatar.com/avatar/41b41a9e23ce9675137f74e0d5bad22c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SumitGupta&#39;s gravatar image" /><p><span>SumitGupta</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SumitGupta has no accepted answers">0%</span></p></div></div><div id="comments-container-58521" class="comments-container"></div><div id="comment-tools-58521" class="comment-tools"></div><div class="clear"></div><div id="comment-58521-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58537"></span>

<div id="answer-container-58537" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58537-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58537-score" class="post-score" title="current number of votes">0</div><span id="post-58537-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It would appear that Wireshark will dissect traffic as <a href="https://en.wikipedia.org/wiki/RDMA_over_Converged_Ethernet">ROCE</a> if:</p><ol><li>The EtherType is 0x8915 (ROCEv1)</li><li>(or) if the UDP port is 4791* (or whatever you set the preference to) (this is for ROCEv2)</li></ol><p>[*] In version 2.2.x and earlier the default UDP port number is 0 so you must set the preference to the right port number. Reference <a href="https://code.wireshark.org/review/#/c/17971/">change 17971</a>.</p><p>If one of those are true and it's still not working we'd need to see the capture file (you can put it someplace like <a href="http://cloudshark.org">Cloudshark</a> or Dropbox).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jan '17, 05:50</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Jan '17, 06:10</strong> </span></p></div></div><div id="comments-container-58537" class="comments-container"><span id="58545"></span><div id="comment-58545" class="comment"><div id="post-58545-score" class="comment-score"></div><div class="comment-text"><p>Thanks. I have uploaded the pcap file to my google drive. Here is the link.</p><p><a href="https://drive.google.com/file/d/0By0m-D3lG9uAMDJGZzd1Q3dxWmM/view?usp=sharing">https://drive.google.com/file/d/0By0m-D3lG9uAMDJGZzd1Q3dxWmM/view?usp=sharing</a></p><p>Also in my case I do not see the "Infiniband" protocol in the wireshark-&gt;preferences ? I only see "Infiniband SDP". I am using the OSX version of wireshark.</p><p>Thanks Sumit</p></div><div id="comment-58545-info" class="comment-info"><span class="comment-age">(05 Jan '17, 13:31)</span> <span class="comment-user userinfo">SumitGupta</span></div></div><span id="58547"></span><div id="comment-58547" class="comment"><div id="post-58547-score" class="comment-score"></div><div class="comment-text"><p>[I converted your answer to a comment--this is a Q&amp;A site, not a forum--see the FAQ.]</p><p>The only non-TCP traffic in that capture file (which I'm presuming is your ROCE traffic) is running over IPv4 with an IP protocol (<code>ip.proto</code>) of 254. That's not a standard way to transport ROCE (at least according to the Wikipedia article referenced in my answer).</p><p>Are you sure that's ROCE traffic? What kind of device is it? Do you know why they're using a non-standard way of transporting ROCE?</p></div><div id="comment-58547-info" class="comment-info"><span class="comment-age">(05 Jan '17, 13:46)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="58548"></span><div id="comment-58548" class="comment"><div id="post-58548-score" class="comment-score"></div><div class="comment-text"><p>Its a mellanox CX-4 adapter. I am running ib_send_lat on 2 mellanox adapters which are connected back to back. On the client side of ib_send_lat, I used the ethtool --set-priv_flag sniffer 1 to set the sniffing for mellanox adapter and then used tcpdump to capture the pcap file.</p><p>Sumit</p></div><div id="comment-58548-info" class="comment-info"><span class="comment-age">(05 Jan '17, 14:00)</span> <span class="comment-user userinfo">SumitGupta</span></div></div><span id="58551"></span><div id="comment-58551" class="comment"><div id="post-58551-score" class="comment-score"></div><div class="comment-text"><p>Oh, to answer your earlier question: the Infiniband dissector is known as <code>IB</code> in the preferences list. It took me a while to find that too.</p><p>It's still not clear to me why your RROCE is running directly over IPv4 rather than UDP. It wouldn't be hard to modify Wireshark do allow you to Decode-As that traffic as IB/RROCE but it would be nice to know how common it is or why it is like that.</p></div><div id="comment-58551-info" class="comment-info"><span class="comment-age">(05 Jan '17, 18:24)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="58580"></span><div id="comment-58580" class="comment"><div id="post-58580-score" class="comment-score"></div><div class="comment-text"><p>I <a href="https://code.wireshark.org/review/19572">submitted a change</a> that will allow you to Decode-As this traffic as RROCE: you need to right-click on the traffic, choose Decode-As, and decode the IP Protocol as IB (Infiniband). You can pick up an <a href="https://www.wireshark.org/download/automated/">automated build</a> to try it out (just choose the latest file). The change will show up in Wireshark 2.4.0 which is expected in the summer.</p></div><div id="comment-58580-info" class="comment-info"><span class="comment-age">(07 Jan '17, 10:46)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-58537" class="comment-tools"></div><div class="clear"></div><div id="comment-58537-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

