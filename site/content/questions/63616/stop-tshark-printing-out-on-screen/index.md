+++
type = "question"
title = "Stop tshark printing out on screen"
description = '''Hello everybody, I&#x27;m using tshark to read a pcap file of Diameter Protocol. Normally, I use &quot;tshark -r&quot;, but doing this, it does not decode the AVP value (&quot; val=%s&quot;) (function &quot;dissect_diameter_avp&quot; in &quot;packet-diameter.c&quot;). When I use option &quot;-T ek&quot;, tshark is able to decode AVP value. But in this w...'''
date = "2017-09-20T03:42:00Z"
lastmod = "2017-09-20T18:26:00Z"
weight = 63616
keywords = [ "avp", "tshark" ]
aliases = [ "/questions/63616" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Stop tshark printing out on screen](/questions/63616/stop-tshark-printing-out-on-screen)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63616-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63616-score" class="post-score" title="current number of votes">0</div><span id="post-63616-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everybody, I'm using tshark to read a pcap file of Diameter Protocol. Normally, I use "tshark -r", but doing this, it does not decode the AVP value (" val=%s") (function "<strong>dissect_diameter_avp</strong>" in "<strong>packet-diameter.c</strong>"). When I use option "-T ek", tshark is able to decode AVP value. But in this way, it prints a lot of information on screen and slow down the performance. Please help me to clarify two problems:</p><ul><li>Can I get AVP value (by coding) without using option "-T ek" ?</li><li>If NOT, is there any way to stop printing out on screen with option "-T ek"?</li></ul><p>Thank you very very much.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-avp" rel="tag" title="see questions tagged &#39;avp&#39;">avp</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Sep '17, 03:42</strong></p><img src="https://secure.gravatar.com/avatar/824a7342f59ff90e6040505b38626416?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hoangsonk49&#39;s gravatar image" /><p><span>hoangsonk49</span><br />
<span class="score" title="81 reputation points">81</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hoangsonk49 has 2 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Sep '17, 03:43</strong> </span></p></div></div><div id="comments-container-63616" class="comments-container"></div><div id="comment-tools-63616" class="comment-tools"></div><div class="clear"></div><div id="comment-63616-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63617"></span>

<div id="answer-container-63617" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63617-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63617-score" class="post-score" title="current number of votes">2</div><span id="post-63617-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hoangsonk49 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not familiar with using <code>-T ek</code>, but if you know the AVP value you're looking for, you can get it with <code>-T fields</code>. For example, suppose you want the <em>Session-Id</em>:</p><pre><code>tshark -r diameter.pcap -Y &quot;diameter.Session-Id&quot; -T fields -e &quot;diameter.Session-Id&quot;</code></pre><p>If you want the value of all AVP's, that's a little harder. I suppose you could run through the file multiple times for each AVP? I don't know what you're trying to do, but here's a script that does that, which may or may not help you:</p><pre><code>#!/bin/sh
# Check usage
if (( ${#} &lt; 1 ))
then
        echo &quot;Usage: $0 &lt;file&gt;&quot;
        exit 0
fi

tshark -r ${1} -Y &quot;diameter.avp.code&quot; -O diameter | grep &quot;AVP Code:&quot; | sed &#39;s/^.*AVP Code: //g&#39; &gt; avp_codes.txt

cat avp_codes.txt | sort | uniq | cut -d &#39; &#39; -f 2 | sort &gt; avp_codes_sorted.txt

avps=`cat avp_codes_sorted.txt`
for avp in ${avps}; do
        field=`echo $avp | tr -d &#39;\r\n&#39;`
        tshark -r ${1} -Y &quot;diameter.$field&quot; -T fields -e &quot;diameter.$field&quot;
done</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '17, 15:20</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-63617" class="comments-container"><span id="63618"></span><div id="comment-63618" class="comment"><div id="post-63618-score" class="comment-score"></div><div class="comment-text"><p>Thank you, cmaynard. My problem solved. Thanks for your very useful support :)</p></div><div id="comment-63618-info" class="comment-info"><span class="comment-age">(20 Sep '17, 18:26)</span> <span class="comment-user userinfo">hoangsonk49</span></div></div></div><div id="comment-tools-63617" class="comment-tools"></div><div class="clear"></div><div id="comment-63617-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

