+++
type = "question"
title = "visited sites filter"
description = '''I need to see the sites visited by a particular ip... m giving that in the filter but it gives me all sort of queries. I hv stared using your product recently and that&#x27;s why I am a little unclear on the kinds of filters to pass. so far i just want to see the sites they visited, what did they searche...'''
date = "2011-03-05T07:51:00Z"
lastmod = "2012-06-11T03:40:00Z"
weight = 2675
keywords = [ "filter" ]
aliases = [ "/questions/2675" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [visited sites filter](/questions/2675/visited-sites-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2675-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2675-score" class="post-score" title="current number of votes">0</div><span id="post-2675-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to see the sites visited by a particular ip... m giving that in the filter but it gives me all sort of queries. I hv stared using your product recently and that's why I am a little unclear on the kinds of filters to pass. so far i just want to see the sites they visited, what did they searched for and what domain names were resolved along with their ip addresses.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Mar '11, 07:51</strong></p><img src="https://secure.gravatar.com/avatar/7c40cee95b99b1fd8174b371672c4b5d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jiya%20Khan&#39;s gravatar image" /><p><span>Jiya Khan</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jiya Khan has no accepted answers">0%</span></p></div></div><div id="comments-container-2675" class="comments-container"></div><div id="comment-tools-2675" class="comment-tools"></div><div class="clear"></div><div id="comment-2675-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2677"></span>

<div id="answer-container-2677" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2677-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2677-score" class="post-score" title="current number of votes">3</div><span id="post-2677-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is all achievable with Wireshark, but Wireshark is not the most intuitive tool for this. Really, you would usually use a web content filter for these types of tasks. If you want to do this with Wireshark, you will first need to add some columns to the display. The columns I would recommend are as follows:</p><p>Host From from the HTTP Get Method URI From the HTTP Get method</p><p>To do this, I would first make sure that you are running at least version 1.4. Then you need to capture some www traffic. Then do a display filter for "http.host". This will display only http requests with host headers. (Note: this is not a perfect method due to the fact that host headers might not be used in obscure cases).<br />
</p><p>Now that we have some packets displayed we need to look for the host field and the uri field. To do this, highlight a packet in the top pane. Then in the middle pane, "Hypertext Transport Protocol", then expand "GET". Right click "Host" and choose "Add as column". Do the same for Request URI. Now in the top pane you should see the host and the path "URI".<br />
</p><p>Now we can filter based on the IP address that you are looking at.</p><p>So to look at www traffic from 192.168.1.124, I might use a filter like: ip.addr==192.168.1.124 &amp;&amp; http.host</p><p>Again, Wireshark is a very granular tool. However it is not a drop in replacement for something like a Barracuda Web Filter or Websense.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '11, 11:55</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p><span>Paul Stewart</span><br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span> </br></br></p></div></div><div id="comments-container-2677" class="comments-container"><span id="2700"></span><div id="comment-2700" class="comment"><div id="post-2700-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much Paul. Can you please guide me a little more about how do we see resolved domain names in a trace file using wireshark? I'll be really grateful.</p></div><div id="comment-2700-info" class="comment-info"><span class="comment-age">(07 Mar '11, 12:19)</span> <span class="comment-user userinfo">Jiya Khan</span></div></div><span id="2701"></span><div id="comment-2701" class="comment"><div id="post-2701-score" class="comment-score"></div><div class="comment-text"><p>When you do the capture you can enable network level name resolutions. This is in Edit &gt; Preferences &gt; Name Resolution "Enable network name resolution". You can also do this in the capture settings. Be aware though that this is a simple PTR lookup. Therefore, if you are looking at web sites, it might make more sense to look at the host header in the get request.</p></div><div id="comment-2701-info" class="comment-info"><span class="comment-age">(07 Mar '11, 12:46)</span> <span class="comment-user userinfo">Paul Stewart</span></div></div><span id="11806"></span><div id="comment-11806" class="comment"><div id="post-11806-score" class="comment-score"></div><div class="comment-text"><p>This is very nice, is it possible to skip repeating hosts?</p></div><div id="comment-11806-info" class="comment-info"><span class="comment-age">(11 Jun '12, 03:40)</span> <span class="comment-user userinfo">besomuk</span></div></div></div><div id="comment-tools-2677" class="comment-tools"></div><div class="clear"></div><div id="comment-2677-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

