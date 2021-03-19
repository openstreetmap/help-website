+++
type = "question"
title = "tshark: Read filters were specified both with &quot;-R&quot; and with additional command-line arguments"
description = '''I&#x27;m facing this problem whenever I run tshark: tshark: Read filters were specified both with &quot;-R&quot; and with additional command-line arguments  My command (run in a script) looks something like this: ./tshark -r $1 -w $2 -R &quot;(frame.time &amp;gt;= &#x27;Mar 21, 2012 14:45:13.000&#x27; &amp;amp;&amp;amp; &#92; frame.time &amp;lt; &#x27;M...'''
date = "2012-03-26T03:35:00Z"
lastmod = "2012-03-26T23:15:00Z"
weight = 9758
keywords = [ "tshark", "display-filter" ]
aliases = [ "/questions/9758" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark: Read filters were specified both with "-R" and with additional command-line arguments](/questions/9758/tshark-read-filters-were-specified-both-with-r-and-with-additional-command-line-arguments)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9758-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9758-score" class="post-score" title="current number of votes">0</div><span id="post-9758-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I'm facing this problem whenever I run <code>tshark</code>:</p><pre><code>tshark: Read filters were specified both with &quot;-R&quot; and with additional command-line arguments</code></pre><p>My command (run in a script) looks something like this:</p><pre><code>./tshark -r $1 -w $2 -R &quot;(frame.time &gt;= &#39;Mar 21, 2012 14:45:13.000&#39;  &amp;&amp;  \
frame.time &lt; &#39;Mar 21, 2012 15:00:13.000&#39;) &amp;&amp; \
(eth.dst==18:80:f5:10:85:08  || eth.dst==ff:ff:ff:ff:ff:ff) &amp;&amp; \
!(eth.src==18:80:f5:10:85:08 ) &amp;&amp; (vlan.id==10 || vlan.id==12)   &amp;&amp; \
!(udp.port&gt;49152 &amp;&amp; !icmp &amp;&amp; !udp.port==55124)&quot; || \
exit 1</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Mar '12, 03:35</strong></p><img src="https://secure.gravatar.com/avatar/6cb6685f12bd537f0f2e1e86a591e940?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sangmeshp&#39;s gravatar image" /><p><span>sangmeshp</span><br />
<span class="score" title="36 reputation points">36</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sangmeshp has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Mar '12, 15:36</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-9758" class="comments-container"></div><div id="comment-tools-9758" class="comment-tools"></div><div class="clear"></div><div id="comment-9758-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9776"></span>

<div id="answer-container-9776" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9776-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9776-score" class="post-score" title="current number of votes">0</div><span id="post-9776-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This worked for me in OSX:</p><pre><code>./tshark -r $1 -w $2 -R &#39;(frame.time &gt;= &quot;Mar 21, 2012 14:45:13.000&quot; &amp;&amp; frame.time &lt; &quot;Mar 21, 2012 15:00:13.000&quot;) &amp;&amp; (eth.dst==18:80:f5:10:85:08  || eth.dst==ff:ff:ff:ff:ff:ff) &amp;&amp; !(eth.src==18:80:f5:10:85:08 ) &amp;&amp; (vlan.id==10 || vlan.id==12)   &amp;&amp; !(udp.port&gt;49152 &amp;&amp; !icmp &amp;&amp; !udp.port==55124)&#39; || exit 1</code></pre><p><strong>Changes:</strong></p><ol><li>Replace your single-quotes around the dates with double-quotes.</li><li>Replace your double-quotes around the super-long display-filter with single-quotes.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Mar '12, 16:01</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-9776" class="comments-container"><span id="9779"></span><div id="comment-9779" class="comment"><div id="post-9779-score" class="comment-score"></div><div class="comment-text"><p>thanks you it worked....</p></div><div id="comment-9779-info" class="comment-info"><span class="comment-age">(26 Mar '12, 22:53)</span> <span class="comment-user userinfo">sangmeshp</span></div></div><span id="9780"></span><div id="comment-9780" class="comment"><div id="post-9780-score" class="comment-score"></div><div class="comment-text"><p>Yes - the only quote mark that can be used in a display filter for quoted strings such as a date and time is the double-quote character; you can't quote strings in a display filter with single quotes, so "Mar 21, 2012 14:45:13.000" is a valid string in a display filter but 'Mar 21, 2012 14:45:13.000' isn't.</p></div><div id="comment-9780-info" class="comment-info"><span class="comment-age">(26 Mar '12, 23:15)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-9776" class="comment-tools"></div><div class="clear"></div><div id="comment-9776-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

