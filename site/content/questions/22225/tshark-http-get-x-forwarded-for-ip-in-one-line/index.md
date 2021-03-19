+++
type = "question"
title = "tshark http get x-forwarded-for ip in one line"
description = '''Hey all, Is it possible to have HTTP GET request and X-forwarded-for IP and the time in 1 single line?  I have difficulties,  tshark -i eth0 -n tcp port 80 -x -R &#x27;http.request.method == &quot;GET&quot;&#x27; | grep &quot;HTTP GET&quot;  0.158435 10.128.99.11 -&amp;gt; 46.12.12.14 HTTP GET /check.html HTTP/1.0  Appreciate any he...'''
date = "2013-06-21T09:53:00Z"
lastmod = "2013-06-21T20:57:00Z"
weight = 22225
keywords = [ "tshark" ]
aliases = [ "/questions/22225" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [tshark http get x-forwarded-for ip in one line](/questions/22225/tshark-http-get-x-forwarded-for-ip-in-one-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22225-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22225-score" class="post-score" title="current number of votes">0</div><span id="post-22225-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey all,</p><p>Is it possible to have HTTP GET request and X-forwarded-for IP and the time in 1 single line?</p><p>I have difficulties,</p><p>tshark -i eth0 -n tcp port 80 -x -R 'http.request.method == "GET"' | grep "HTTP GET"</p><p>0.158435 10.128.99.11 -&gt; 46.12.12.14 HTTP GET /check.html HTTP/1.0</p><p>Appreciate any help given.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jun '13, 09:53</strong></p><img src="https://secure.gravatar.com/avatar/72758a015ff182650c5d36355fb0223b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="diden&#39;s gravatar image" /><p><span>diden</span><br />
<span class="score" title="8 reputation points">8</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="diden has no accepted answers">0%</span></p></div></div><div id="comments-container-22225" class="comments-container"></div><div id="comment-tools-22225" class="comment-tools"></div><div class="clear"></div><div id="comment-22225-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22229"></span>

<div id="answer-container-22229" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22229-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22229-score" class="post-score" title="current number of votes">1</div><span id="post-22229-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try this after capturing and saving the file.</p><p>tshark -r &lt;yourpcap&gt; -Tfields -e "http.request.method==GET" -e "http.request.uri" -e "http.x_forwarded_for" -e frame.time_relative</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '13, 13:37</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Jun '13, 14:31</strong> </span></p></div></div><div id="comments-container-22229" class="comments-container"></div><div id="comment-tools-22229" class="comment-tools"></div><div class="clear"></div><div id="comment-22229-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22236"></span>

<div id="answer-container-22236" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22236-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22236-score" class="post-score" title="current number of votes">1</div><span id="post-22236-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If they're in the same packet, from a live capture (Note: from this example you can add any container that you want to display as a column just by adding more -e's):</p><p>tshark -i eth0 -R 'tcp.port==80&amp;&amp;http.request.method=="GET"&amp;&amp;http.x_forwarded_for' -T fields -e frame.time -e http.request.method -e http.request.uri</p><p>The other answer will work, except that your initial capture was with a display filter. You can not save a live capture in tshark while using a display filter on it, so the result of the other answer's output would be the lines you want, plus a lot of unwanted empty space for packets which match your unfiltered -r request on the whole trace but don't have the fields you're looking for. Another way to do it would be to save with a capture filter then read it against a display filter but in this case you can do it in one step since you're just looking for the field output on a live capture.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '13, 19:01</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Jun '13, 19:12</strong> </span></p></div></div><div id="comments-container-22236" class="comments-container"><span id="22239"></span><div id="comment-22239" class="comment"><div id="post-22239-score" class="comment-score"></div><div class="comment-text"><p>Yes you are right that i need a live capture on screen.</p><p>I tried the following but did not see the x-forwarded-ip. Am i missing something ?</p><p>tshark -i eth0 -R 'tcp.port==80&amp;&amp;http.request.method=="GET"&amp;&amp;http.x_forwarded_for' -T fields -e frame.time -e http.request.method -e http.request.uri</p></div><div id="comment-22239-info" class="comment-info"><span class="comment-age">(21 Jun '13, 20:55)</span> <span class="comment-user userinfo">diden</span></div></div><span id="22240"></span><div id="comment-22240" class="comment"><div id="post-22240-score" class="comment-score"></div><div class="comment-text"><p>I found what i needed with both your help. Thanks.</p><p>tshark -i eth0 -R 'tcp.port==80&amp;&amp;http.request.method=="GET"&amp;&amp;http.x_forwarded_for' -T fields -e http.x_forwarded_for -e frame.time -e http.request.method -e http.request.uri</p></div><div id="comment-22240-info" class="comment-info"><span class="comment-age">(21 Jun '13, 20:57)</span> <span class="comment-user userinfo">diden</span></div></div></div><div id="comment-tools-22236" class="comment-tools"></div><div class="clear"></div><div id="comment-22236-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

