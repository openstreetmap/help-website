+++
type = "question"
title = "Wireshark not recognizing port 8888 HTTP traffic as HTTP"
description = '''Hello, I can&#x27;t capture http localhost traffic under Ubuntu: it does not display anything. It works with wlan0 but not with loopback 127.0.0.1. I probably missed something but can&#x27;t figure out what. Could someone helps? Thanks PS: I can see the localhost http traffic under Chromium developer&#x27;s tool n...'''
date = "2012-07-07T05:35:00Z"
lastmod = "2012-07-09T09:03:00Z"
weight = 12497
keywords = [ "loopback", "http", "ubuntu" ]
aliases = [ "/questions/12497" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark not recognizing port 8888 HTTP traffic as HTTP](/questions/12497/wireshark-not-recognizing-port-8888-http-traffic-as-http)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12497-score" class="post-score" title="current number of votes">0</div><span id="post-12497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I can't capture http localhost traffic under Ubuntu: it does not display anything.</p><p>It works with wlan0 but not with loopback 127.0.0.1. I probably missed something but can't figure out what.</p><p>Could someone helps? Thanks</p><p>PS: I can see the localhost http traffic under Chromium developer's tool network tab.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-loopback" rel="tag" title="see questions tagged &#39;loopback&#39;">loopback</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jul '12, 05:35</strong></p><img src="https://secure.gravatar.com/avatar/f1752ab01f6adb1eb122f54194461335?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Grangousier&#39;s gravatar image" /><p><span>Grangousier</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Grangousier has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Jul '12, 11:43</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-12497" class="comments-container"><span id="12500"></span><div id="comment-12500" class="comment"><div id="post-12500-score" class="comment-score"></div><div class="comment-text"><p>So you're connecting from an HTTP client (such as a Web browser) on your machine to an HTTP server on your machine, and you're not seeing any traffic even though the HTTP client <em>is</em> fetching stuff from the server?</p><p>What version of the kernel is your Ubuntu machine running (<code>uname -r</code>)?</p></div><div id="comment-12500-info" class="comment-info"><span class="comment-age">(07 Jul '12, 15:01)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="12501"></span><div id="comment-12501" class="comment"><div id="post-12501-score" class="comment-score"></div><div class="comment-text"><blockquote><p>it does not display anything.</p></blockquote><p>what does it display?</p></div><div id="comment-12501-info" class="comment-info"><span class="comment-age">(07 Jul '12, 16:11)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="12503"></span><div id="comment-12503" class="comment"><div id="post-12503-score" class="comment-score"></div><div class="comment-text"><p>Yes I have a local jetty server that runs my application and I connect to it using chromium but no http traffic is displayed by wireshark, whereas several http requests and responses are exchanged between the client and the server.</p><p>My ubuntu kernel version is 2.6.38-15-generic-pae. It's an old version but I fought so much to get Ubuntu run on my sony vaio one year ago (lots of problems with graphic support) that I hesitate to upgrade it.</p></div><div id="comment-12503-info" class="comment-info"><span class="comment-age">(08 Jul '12, 01:48)</span> <span class="comment-user userinfo">Grangousier</span></div></div><span id="12505"></span><div id="comment-12505" class="comment"><div id="post-12505-score" class="comment-score"></div><div class="comment-text"><p>what is the ubuntu release (lsb_release -a)?<br />
How did you access the local server? 127.0.0.1 or the interface IP?<br />
Did you set a capture filter?<br />
Do you see the traffic if you capture with tcpdump?</p></div><div id="comment-12505-info" class="comment-info"><span class="comment-age">(08 Jul '12, 02:05)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="12506"></span><div id="comment-12506" class="comment"><div id="post-12506-score" class="comment-score"></div><div class="comment-text"><p>Kurt, When I said "it does not display anything" I actually meant it does not display any "http" traffic but "tcp" traffic is displayed with source and destination address being 127.0.0.1.</p></div><div id="comment-12506-info" class="comment-info"><span class="comment-age">(08 Jul '12, 02:11)</span> <span class="comment-user userinfo">Grangousier</span></div></div><span id="12507"></span><div id="comment-12507" class="comment not_top_scorer"><div id="post-12507-score" class="comment-score"></div><div class="comment-text"><p>tcp traffic on which port?</p></div><div id="comment-12507-info" class="comment-info"><span class="comment-age">(08 Jul '12, 02:37)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="12509"></span><div id="comment-12509" class="comment not_top_scorer"><div id="post-12509-score" class="comment-score"></div><div class="comment-text"><p>what is the ubuntu release (lsb_release -a)? 11.04</p><p>Did you set a capture filter? No capture filter</p><p>Do you see the traffic if you capture with tcpdump? Yes. I also see the tcp traffic with wireshark.</p><p>How did you access the local server? 127.0.0.1 or the interface IP? I don't understand what you mean by "access with interface IP"! I access it using a web browser where I enter my url "http://127.0.0.1:8888/"</p></div><div id="comment-12509-info" class="comment-info"><span class="comment-age">(08 Jul '12, 03:08)</span> <span class="comment-user userinfo">Grangousier</span></div></div></div><div id="comment-tools-12497" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-12497-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12508"></span>

<div id="answer-container-12508" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12508-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12508-score" class="post-score" title="current number of votes">2</div><span id="post-12508-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Grangousier has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>According to the information you provided so far, I believe your web server runs on a port that is not detected as HTTP by Wireshark. If so,</p><ul><li>either right click any packet of the communication an select "Decode as" (then select HTTP)</li><li>or add your application port to the HTTP dissector preferences:</li></ul><blockquote><p><code>Edit -&gt; Preferences -&gt; Protocols -&gt; HTTP -&gt; TCP Ports</code></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '12, 02:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-12508" class="comments-container"><span id="12510"></span><div id="comment-12510" class="comment"><div id="post-12510-score" class="comment-score"></div><div class="comment-text"><p>Beautiful,</p><p>I added the port 8888 and it works now.</p><p>Thanks a lot Kurt.</p></div><div id="comment-12510-info" class="comment-info"><span class="comment-age">(08 Jul '12, 03:13)</span> <span class="comment-user userinfo">Grangousier</span></div></div><span id="12530"></span><div id="comment-12530" class="comment"><div id="post-12530-score" class="comment-score"></div><div class="comment-text"><p><span>@Grangousier</span>: If this is the correct answer than please tick the check mark to indicate so. That's proper Q&amp;A etiquette.</p></div><div id="comment-12530-info" class="comment-info"><span class="comment-age">(09 Jul '12, 09:03)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-12508" class="comment-tools"></div><div class="clear"></div><div id="comment-12508-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

