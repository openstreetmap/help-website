+++
type = "question"
title = "how to get the x-cache field in tshark ?"
description = '''hi  I have a pcap file with some packets coming from squid cache.  looking at wireshark, I can view the x-cache header under the HTTP section. however, I can not find an equivalent field for tshark . I have tried composing a lua listener to extract the info myself , but the tvb field is NIL for all ...'''
date = "2011-12-28T00:32:00Z"
lastmod = "2011-12-28T22:40:00Z"
weight = 8149
keywords = [ "http", "tshark", "x-cache" ]
aliases = [ "/questions/8149" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [how to get the x-cache field in tshark ?](/questions/8149/how-to-get-the-x-cache-field-in-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8149-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8149-score" class="post-score" title="current number of votes">0</div><span id="post-8149-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi I have a pcap file with some packets coming from squid cache. looking at wireshark, I can view the x-cache header under the HTTP section. however, I can not find an equivalent field for tshark . I have tried composing a lua listener to extract the info myself , but the tvb field is NIL for all packets . can anyone help ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-x-cache" rel="tag" title="see questions tagged &#39;x-cache&#39;">x-cache</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Dec '11, 00:32</strong></p><img src="https://secure.gravatar.com/avatar/7eff7b23646c5be465e00815aabcf9b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yoav&#39;s gravatar image" /><p><span>yoav</span><br />
<span class="score" title="86 reputation points">86</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yoav has no accepted answers">0%</span></p></div></div><div id="comments-container-8149" class="comments-container"><span id="8150"></span><div id="comment-8150" class="comment"><div id="post-8150-score" class="comment-score"></div><div class="comment-text"><p>do you just want to extract the text inside HTTP stating "X-Cache..."?</p></div><div id="comment-8150-info" class="comment-info"><span class="comment-age">(28 Dec '11, 07:34)</span> <span class="comment-user userinfo">Landi</span></div></div></div><div id="comment-tools-8149" class="comment-tools"></div><div class="clear"></div><div id="comment-8149-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="8153"></span>

<div id="answer-container-8153" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8153-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8153-score" class="post-score" title="current number of votes">3</div><span id="post-8153-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="yoav has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can add custom http header fields to the HTTP preferences setting, which will then allow you to access them (also as a filter, which won't be available without adding it to the preferences first). Gerald wrote an answer to a similar question here, which might help:</p><p><a href="http://ask.wireshark.org/questions/816/tshark-custom-http-headers">http://ask.wireshark.org/questions/816/tshark-custom-http-headers</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Dec '11, 07:43</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Dec '11, 07:44</strong> </span></p></div></div><div id="comments-container-8153" class="comments-container"><span id="8160"></span><div id="comment-8160" class="comment"><div id="post-8160-score" class="comment-score"></div><div class="comment-text"><p>thanks ! this was well hidden - but it sure works :-)</p></div><div id="comment-8160-info" class="comment-info"><span class="comment-age">(28 Dec '11, 22:40)</span> <span class="comment-user userinfo">yoav</span></div></div></div><div id="comment-tools-8153" class="comment-tools"></div><div class="clear"></div><div id="comment-8153-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8151"></span>

<div id="answer-container-8151" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8151-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8151-score" class="post-score" title="current number of votes">0</div><span id="post-8151-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>X-Cache is not a <a href="http://www.wireshark.org/docs/dfref/h/http.html">filterable field</a>, but you can use TShark and awk or grep:<br />
</p><pre><code>$ tshark -r clmt_04.pcap -R &quot;http contains X-&quot; -O http -V | awk &#39;/X-/ {print}&#39; &gt; X-.txt
$ tshark -r clmt_04.pcap -R &quot;http contains X-&quot; -O http -V | awk &#39;/X-Cache/ {print}&#39; &gt; X-Cache1.txt
$ tshark -r clmt_04.pcap -R &quot;http contains X-&quot; -O http -V | grep X-Cache &gt; X-Cache2.txt</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Dec '11, 07:39</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p><span>joke</span><br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></p></div></div><div id="comments-container-8151" class="comments-container"><span id="8155"></span><div id="comment-8155" class="comment"><div id="post-8155-score" class="comment-score"></div><div class="comment-text"><p>In addition to Jasper's answer.<br />
After adding a custom http header field:<br />
</p><pre><code>$ tshark -r clmt_04.pcap -T fields -e frame.number -e http.header.X-Cache &gt; http.header.X-Cache.txt
$ tshark -i 3 -T fields -e frame.number -e http.header.X-Cache -E header=y -E separator=, &gt; http.header.X-Cache2.csv</code></pre></div><div id="comment-8155-info" class="comment-info"><span class="comment-age">(28 Dec '11, 13:01)</span> <span class="comment-user userinfo">joke</span></div></div></div><div id="comment-tools-8151" class="comment-tools"></div><div class="clear"></div><div id="comment-8151-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

