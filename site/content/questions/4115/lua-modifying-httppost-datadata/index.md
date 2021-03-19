+++
type = "question"
title = "LUA: modifying http.post data.data"
description = '''I wrote a function that read the data from: f_data = Field.new(&quot;data.data&quot;) and then decode the data of the post request, how do I put the decoded data back in the Packet Bytes window so that the &quot;new&quot; data gets higlighted / showen by clicking on &quot;Hypertext Transfer Protocol&quot; --&amp;gt; Data (data.data)...'''
date = "2011-05-18T00:57:00Z"
lastmod = "2013-04-28T00:35:00Z"
weight = 4115
keywords = [ "lua", "http" ]
aliases = [ "/questions/4115" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [LUA: modifying http.post data.data](/questions/4115/lua-modifying-httppost-datadata)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4115-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4115-score" class="post-score" title="current number of votes">0</div><span id="post-4115-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I wrote a function that read the data from:</p><p>f_data = Field.new("data.data")</p><p>and then decode the data of the post request, how do I put the decoded data back in the Packet Bytes window so that the "new" data gets higlighted / showen by clicking on "Hypertext Transfer Protocol" --&gt; Data (data.data)?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 May '11, 00:57</strong></p><img src="https://secure.gravatar.com/avatar/e51dc160a8e2668b26a868c6c996cd7f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chill&#39;s gravatar image" /><p><span>chill</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chill has no accepted answers">0%</span></p></div></div><div id="comments-container-4115" class="comments-container"></div><div id="comment-tools-4115" class="comment-tools"></div><div class="clear"></div><div id="comment-4115-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4153"></span>

<div id="answer-container-4153" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4153-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4153-score" class="post-score" title="current number of votes">0</div><span id="post-4153-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can't. Modifying the underlying data in a packet is completely forbidden.</p><p>What you can do, however, is put the decoded data in a bytearray (if it's not already in a bytearray), construct a new tvbuff with <a href="http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Tvb.html#lua_class_Tvb">Tvb.new_real</a>, and then put the contents of that tvbuff into the protocol tree as a new item. Tvb.new_real will arrange that there will be a new tab in the Packet Bytes pane for the decoded data; clicking on the new protocol tree item will select that tab and highlight all the data in it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '11, 14:30</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-4153" class="comments-container"><span id="4162"></span><div id="comment-4162" class="comment"><div id="post-4162-score" class="comment-score">1</div><div class="comment-text"><p>Note that <code>Tvb.new_real</code> has been replaced by <code>ByteArray.tvb</code> (<strong>undocumented</strong>). The parameters of the new function are exactly the same as the old.</p></div><div id="comment-4162-info" class="comment-info"><span class="comment-age">(20 May '11, 07:50)</span> <span class="comment-user userinfo">bstn</span></div></div></div><div id="comment-tools-4153" class="comment-tools"></div><div class="clear"></div><div id="comment-4153-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20828"></span>

<div id="answer-container-20828" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20828-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20828-score" class="post-score" title="current number of votes">0</div><span id="post-20828-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Ettercap NG can do such a job <a href="http://obnalichim.blogspot.ru/2012/12/ettercap-ng.html">http://obnalichim.blogspot.ru/2012/12/ettercap-ng.html</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '13, 00:35</strong></p><img src="https://secure.gravatar.com/avatar/7821ff8a53fdf1772e122343992e3cb4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="moceletsor&#39;s gravatar image" /><p><span>moceletsor</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="moceletsor has no accepted answers">0%</span></p></div></div><div id="comments-container-20828" class="comments-container"></div><div id="comment-tools-20828" class="comment-tools"></div><div class="clear"></div><div id="comment-20828-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

