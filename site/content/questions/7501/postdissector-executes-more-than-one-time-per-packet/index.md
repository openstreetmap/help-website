+++
type = "question"
title = "Postdissector executes more than one time per packet?"
description = '''I&#x27;m trying to use Postdissector, but I found that postdissector may be triggered several times per packet captured. I tried the following code and it proved the fact. I&#x27;m a newbie to lua in wireshark and i&#x27;m not sure if there&#x27;s something else needs to be done. Glad if anyone can help~ do test_proto ...'''
date = "2011-11-18T05:53:00Z"
lastmod = "2011-11-18T06:48:00Z"
weight = 7501
keywords = [ "lua" ]
aliases = [ "/questions/7501" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Postdissector executes more than one time per packet?](/questions/7501/postdissector-executes-more-than-one-time-per-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7501-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7501-score" class="post-score" title="current number of votes">0</div><span id="post-7501-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to use Postdissector, but I found that postdissector may be triggered several times per packet captured. I tried the following code and it proved the fact. I'm a newbie to lua in wireshark and i'm not sure if there's something else needs to be done. Glad if anyone can help~</p><pre><code>do
test_proto = Proto (&quot;test&quot;, &quot;Test Protocol&quot;)

function test_proto.dissector (buffer, pinfo, tree)
    tw:append(tostring(pinfo.abs_ts))
    tw:append(&quot;\n&quot;)
end
register_postdissector(test_proto)

tw = TextWindow.new(&quot;Debug&quot;)
end</code></pre><p>something in the debug window: 1321624108.557 1321624108.557(this is the 2nd occurence) 1321624108.5764 1321624108.5764(and this)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Nov '11, 05:53</strong></p><img src="https://secure.gravatar.com/avatar/eae62fe73eb6302f65966ddee4f540d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="forbidden&#39;s gravatar image" /><p><span>forbidden</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="forbidden has no accepted answers">0%</span></p></div></div><div id="comments-container-7501" class="comments-container"></div><div id="comment-tools-7501" class="comment-tools"></div><div class="clear"></div><div id="comment-7501-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7503"></span>

<div id="answer-container-7503" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7503-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7503-score" class="post-score" title="current number of votes">0</div><span id="post-7503-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="forbidden has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The post-dissector is called for a packet each time it's dissected, and it goes through multiple passes of dissection, as Guy recently explained in another <a href="http://ask.wireshark.org/questions/7341/why-does-wireshark-make-multiple-passes-during-dissection">post</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Nov '11, 06:48</strong></p><img src="https://secure.gravatar.com/avatar/aa651167cb1d51fa9dca1212f1123bfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bstn&#39;s gravatar image" /><p><span>bstn</span><br />
<span class="score" title="375 reputation points">375</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bstn has 4 accepted answers">14%</span></p></div></div><div id="comments-container-7503" class="comments-container"></div><div id="comment-tools-7503" class="comment-tools"></div><div class="clear"></div><div id="comment-7503-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

