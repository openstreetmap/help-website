+++
type = "question"
title = "Merge two files without repeating the same traffic twice."
description = '''Hello, I have the toplology as below.  Host1-(eth1)------ Switch ----(eth2)-Host2  |  |  (eth3)  host3  Some traffic is flowing between Host1 and Host2 and Host3. I dont have an access to the switch. I have captured the traffic at eth1 of Host1 and eth2 of Host2 and eth3 of Host3. It is more than a ...'''
date = "2014-08-26T15:42:00Z"
lastmod = "2014-08-27T07:03:00Z"
weight = 35780
keywords = [ "tcpdump", "capture-file-merge", "tshark", "wireshark" ]
aliases = [ "/questions/35780" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Merge two files without repeating the same traffic twice.](/questions/35780/merge-two-files-without-repeating-the-same-traffic-twice)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35780-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have the toplology as below.</p><p>Host1-(eth1)------ Switch ----(eth2)-Host2</p><pre><code>                       |
                       |
                     (eth3)
                     host3</code></pre><p>Some traffic is flowing between Host1 and Host2 and Host3. I dont have an access to the switch. I have captured the traffic at eth1 of Host1 and eth2 of Host2 and eth3 of Host3. It is more than a 1GB of file.<br />
</p><p>When Host1 sends a traffic to host2 ,traffic is captured at eth1 and eth2 is almost same. I want to know how much is the total traffic flowing in this cluster when running particular job.</p><p>So I combine this two wireshark pcap file</p><p>I have merged two file using mergecap -w new.pcap eth1.pcap eth2.pcap</p><p>But I think it just add this two file and it is same data twice. How can i have all the captured file in a single file without repeating the same traffic twice.</p><p>Thanks in advance!</p><p>Thanks Navaz</p></div><div id="question-tags" class="tags-container tags">tcpdump capture-file-merge tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Aug '14, 15:42</strong></p><img src="https://secure.gravatar.com/avatar/7ebc4294ff0928fd4def898edda41aae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="navaz&#39;s gravatar image" /><p>navaz<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="navaz has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Sep '14, 22:30</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-35780" class="comments-container"></div><div id="comment-tools-35780" class="comment-tools"></div><div class="clear"></div><div id="comment-35780-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35806"></span>

<div id="answer-container-35806" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35806-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The best solution would be to <strong>not</strong> capture the same traffic at both endpoints, as there is no benefit doing so in your environment. Anyway, if you don't want to (or can't) change that, here is what you can do:</p><ul><li>merge the two capture files with mergecap</li><li>remove duplicates with editcap (see man page), like this: <strong>editcap -D 20 input.pcap output.pcap</strong></li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '14, 07:03</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-35806" class="comments-container"><span id="35817"></span><div id="comment-35817" class="comment"><div id="post-35817-score" class="comment-score"></div><div class="comment-text"><p>Thank you Kurt for your response. I have used the above command editcap -D 20 in out , which removed only few packets. What is the number "20" ? I checked the man and it says "window size" . How can we know what window size we need to chose? Its between 1 to 1000000 ? How does it effect the result ?</p></div><div id="comment-35817-info" class="comment-info"><span class="comment-age">(27 Aug '14, 13:25)</span> navaz</div></div></div><div id="comment-tools-35806" class="comment-tools"></div><div class="clear"></div><div id="comment-35806-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

