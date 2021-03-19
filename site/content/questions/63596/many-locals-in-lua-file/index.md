+++
type = "question"
title = "many locals in lua file"
description = '''Hello, I&#x27;m writing a tool that transfers some XML file into a LUA file. The XML file contains above 100 messages. I have to have as minimum following 2 statements for each message: local p_multi = Proto(&quot;multi&quot;, &quot;MultiProto&quot;); local f=p_multi.fields  meaning that I have at least 200 &#x27;local&#x27; records ...'''
date = "2017-09-13T21:55:00Z"
lastmod = "2017-10-04T07:08:00Z"
weight = 63596
keywords = [ "local" ]
aliases = [ "/questions/63596" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [many locals in lua file](/questions/63596/many-locals-in-lua-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63596-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63596-score" class="post-score" title="current number of votes">0</div><span id="post-63596-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm writing a tool that transfers some XML file into a LUA file. The XML file contains above 100 messages.</p><p>I have to have as minimum following 2 statements for each message:</p><pre><code>local p_multi = Proto(&quot;multi&quot;, &quot;MultiProto&quot;);
local f=p_multi.fields</code></pre><p>meaning that I have at least 200 'local' records which is limited by LUA. I've tried to use it as follows, but getting an error:</p><pre><code>local locals={}
locals.p_multi = Proto(&quot;multi&quot;, &quot;MultiProto&quot;);
locals.f=p_multi.fields</code></pre><p>I've also tried to remove the local statement, but in Wireshark I've received an empty message content (i.e all the fields were with null value)</p><pre><code>p_multi = Proto(&quot;multi&quot;, &quot;MultiProto&quot;);
f=p_multi.fields</code></pre><p>Any suggestion how to solve it?</p><p>Thank you :)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-local" rel="tag" title="see questions tagged &#39;local&#39;">local</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Sep '17, 21:55</strong></p><img src="https://secure.gravatar.com/avatar/b02c5dfff2049bed61dbced93bf455d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BMWE&#39;s gravatar image" /><p><span>BMWE</span><br />
<span class="score" title="46 reputation points">46</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BMWE has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Sep '17, 22:00</strong> </span></p></div></div><div id="comments-container-63596" class="comments-container"><span id="63597"></span><div id="comment-63597" class="comment"><div id="post-63597-score" class="comment-score"></div><div class="comment-text"><p>I've found how can I reduce to a single local instead of two. but this still can be problematic as number of messages can be above 200 (different small messages send on the network).</p></div><div id="comment-63597-info" class="comment-info"><span class="comment-age">(13 Sep '17, 22:12)</span> <span class="comment-user userinfo">BMWE</span></div></div></div><div id="comment-tools-63596" class="comment-tools"></div><div class="clear"></div><div id="comment-63596-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63601"></span>

<div id="answer-container-63601" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63601-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63601-score" class="post-score" title="current number of votes">0</div><span id="post-63601-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cmaynard has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Replacing <code>locals.f=p_multi.fields</code> with <code>locals.f=locals.p_multi.fields</code> and doing same in all relevant places solved the issue</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Sep '17, 01:48</strong></p><img src="https://secure.gravatar.com/avatar/b02c5dfff2049bed61dbced93bf455d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BMWE&#39;s gravatar image" /><p><span>BMWE</span><br />
<span class="score" title="46 reputation points">46</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BMWE has one accepted answer">100%</span></p></div></div><div id="comments-container-63601" class="comments-container"><span id="63698"></span><div id="comment-63698" class="comment"><div id="post-63698-score" class="comment-score"></div><div class="comment-text"><p>Hello, I am also generating lua dissectors. Do you mind me asking what these are for?</p><p>Maybe we could share some knowledge. Here are a few examples:</p><p><a href="https://github.com/Open-Markets-Initiative/wireshark-lua">https://github.com/Open-Markets-Initiative/wireshark-lua</a></p><p>Bill</p></div><div id="comment-63698-info" class="comment-info"><span class="comment-age">(03 Oct '17, 13:13)</span> <span class="comment-user userinfo">william</span></div></div><span id="63699"></span><div id="comment-63699" class="comment"><div id="post-63699-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>Having a glimpse on your work and it seems good. I'll have some additional look later.</p></div><div id="comment-63699-info" class="comment-info"><span class="comment-age">(04 Oct '17, 07:08)</span> <span class="comment-user userinfo">BMWE</span></div></div></div><div id="comment-tools-63601" class="comment-tools"></div><div class="clear"></div><div id="comment-63601-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

