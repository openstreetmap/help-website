+++
type = "question"
title = "how to read a specific octet from the dest IP in Lua"
description = '''What&#x27;s the Lua to get a specific octet out of the destination IP address of a packet?'''
date = "2012-02-14T01:32:00Z"
lastmod = "2012-02-16T03:31:00Z"
weight = 8990
keywords = [ "lua" ]
aliases = [ "/questions/8990" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how to read a specific octet from the dest IP in Lua](/questions/8990/how-to-read-a-specific-octet-from-the-dest-ip-in-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8990-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8990-score" class="post-score" title="current number of votes">0</div><span id="post-8990-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What's the Lua to get a specific octet out of the destination IP address of a packet?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Feb '12, 01:32</strong></p><img src="https://secure.gravatar.com/avatar/912ebc145cb38ec3da99be6003d7d9b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Leena&#39;s gravatar image" /><p><span>Leena</span><br />
<span class="score" title="51 reputation points">51</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Leena has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Feb '12, 06:06</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-8990" class="comments-container"><span id="8996"></span><div id="comment-8996" class="comment"><div id="post-8996-score" class="comment-score"></div><div class="comment-text"><p>By "check", do you mean "get the value of"?</p><p>Where is this IP from? The source IP address of a packet? A buffer? An <code>Address</code> variable?</p></div><div id="comment-8996-info" class="comment-info"><span class="comment-age">(14 Feb '12, 09:35)</span> <span class="comment-user userinfo">bstn</span></div></div><span id="9010"></span><div id="comment-9010" class="comment"><div id="post-9010-score" class="comment-score"></div><div class="comment-text"><p>I get the ip address from wireshark using lua and then I want to be free in making any process I want in each octet in the destination ip address with Lua.</p></div><div id="comment-9010-info" class="comment-info"><span class="comment-age">(14 Feb '12, 23:34)</span> <span class="comment-user userinfo">Leena</span></div></div></div><div id="comment-tools-8990" class="comment-tools"></div><div class="clear"></div><div id="comment-8990-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9046"></span>

<div id="answer-container-9046" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9046-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9046-score" class="post-score" title="current number of votes">1</div><span id="post-9046-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Leena has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The packet's IP destination is contained in <a href="http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Pinfo.html#lua_class_Pinfo"><code>pinfo.dst</code></a>, which is an <a href="http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Pinfo.html#lua_class_Address"><code>Address</code></a>, which only gives the string representation of the IP address. You can use <a href="http://lua-users.org/wiki/PatternsTutorial">Lua patterns</a> (similar to regular expressions) to parse the individual octets from the IP address, as shown in the following example:</p><pre><code>function tap.packet(pinfo, buffer)
    local ip = tostring(pinfo.dst)
    local o1,o2,o3,o4 = ip:match(&quot;(%d%d?%d?)%.(%d%d?%d?)%.(%d%d?%d?)%.(%d%d?%d?)&quot; )
    print(o1,o2,o3,o4)
end</code></pre><p>Note that the values (<code>o1</code>, <code>o2</code>, etc.) are of <code>string</code> type. Use <code>number</code> conversion if necessary (i.e., <code>tonumber(o1)</code>, <code>tonumber(o2)</code>, etc.).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '12, 14:58</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-9046" class="comments-container"><span id="9052"></span><div id="comment-9052" class="comment"><div id="post-9052-score" class="comment-score"></div><div class="comment-text"><p>Thanks very much Helloworld, you always helps me a lot.</p></div><div id="comment-9052-info" class="comment-info"><span class="comment-age">(15 Feb '12, 23:00)</span> <span class="comment-user userinfo">Leena</span></div></div><span id="9056"></span><div id="comment-9056" class="comment"><div id="post-9056-score" class="comment-score"></div><div class="comment-text"><p>Please accept the answer by clicking on the "tick" if it solves your issue.</p></div><div id="comment-9056-info" class="comment-info"><span class="comment-age">(16 Feb '12, 03:31)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-9046" class="comment-tools"></div><div class="clear"></div><div id="comment-9046-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

