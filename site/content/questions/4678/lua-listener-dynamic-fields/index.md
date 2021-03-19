+++
type = "question"
title = "Lua listener, dynamic fields"
description = '''Hello, I have a listener that needs to get field value dynamically. Since Field_new can only be used outside of a tap I tried using all_field_infos() which does work like this: fields = { all_field_infos() } This gives me an array of field_info objects of the upper most protocols in the tree, the pr...'''
date = "2011-06-22T13:53:00Z"
lastmod = "2013-02-17T07:47:00Z"
weight = 4678
keywords = [ "listener", "lua", "tap", "fields" ]
aliases = [ "/questions/4678" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Lua listener, dynamic fields](/questions/4678/lua-listener-dynamic-fields)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4678-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4678-score" class="post-score" title="current number of votes">0</div><span id="post-4678-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have a listener that needs to get field value dynamically. Since Field_new can only be used outside of a tap I tried using all_field_infos() which does work like this: fields = { all_field_infos() }</p><p>This gives me an array of field_info objects of the upper most protocols in the tree, the problem is I can't figure out how to walk over the branches.</p><p>Seems like this function lacks documentation, or is not really meant to be used.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-listener" rel="tag" title="see questions tagged &#39;listener&#39;">listener</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-tap" rel="tag" title="see questions tagged &#39;tap&#39;">tap</span> <span class="post-tag tag-link-fields" rel="tag" title="see questions tagged &#39;fields&#39;">fields</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jun '11, 13:53</strong></p><img src="https://secure.gravatar.com/avatar/6491d13e779b556cdc1f1d13e76c0a9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Demon&#39;s gravatar image" /><p><span>Demon</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Demon has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> retagged <strong>23 Jun '11, 19:49</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-4678" class="comments-container"><span id="5104"></span><div id="comment-5104" class="comment"><div id="post-5104-score" class="comment-score"></div><div class="comment-text"><p>It turns out that <code>all_field_infos()</code> behaves differently in a tap/listener than a postdissector. The function correctly enumerates all fields in the postdissector while it only includes the header fields in the tap. This is likely a bug.</p></div><div id="comment-5104-info" class="comment-info"><span class="comment-age">(18 Jul '11, 07:55)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="5704"></span><div id="comment-5704" class="comment"><div id="post-5704-score" class="comment-score"></div><div class="comment-text"><p>Weird. Did you open a bug report, or should I?</p></div><div id="comment-5704-info" class="comment-info"><span class="comment-age">(15 Aug '11, 08:20)</span> <span class="comment-user userinfo">Demon</span></div></div><span id="5719"></span><div id="comment-5719" class="comment"><div id="post-5719-score" class="comment-score"></div><div class="comment-text"><p>No, I haven't opened a bug for it (you can do it).</p></div><div id="comment-5719-info" class="comment-info"><span class="comment-age">(16 Aug '11, 23:19)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="5735"></span><div id="comment-5735" class="comment"><div id="post-5735-score" class="comment-score"></div><div class="comment-text"><p>I will soon. Thank you for your time.</p></div><div id="comment-5735-info" class="comment-info"><span class="comment-age">(18 Aug '11, 01:32)</span> <span class="comment-user userinfo">Demon</span></div></div></div><div id="comment-tools-4678" class="comment-tools"></div><div class="clear"></div><div id="comment-4678-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18555"></span>

<div id="answer-container-18555" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18555-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18555-score" class="post-score" title="current number of votes">1</div><span id="post-18555-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think it's a bug - it's by design. And it happens for both Listeners and Dissectors. The problem is packets aren't fully dissected - or rather their field trees aren't created - until you select a packet. So when a tap Listener is called in Lua, the proto tree hasn't been fully created; and likewise for when a dissector is called. It just happens that a dissector will be called multiple times, including when the user selects a packet and thus when the full tree is available.</p><p>I've added an example script to show this happening, titled "View Packet Tree of Fields/FieldInfo" in here: <a href="http://wiki.wireshark.org/Lua/Examples">http://wiki.wireshark.org/Lua/Examples</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '13, 08:45</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-18555" class="comments-container"><span id="18567"></span><div id="comment-18567" class="comment"><div id="post-18567-score" class="comment-score"></div><div class="comment-text"><p>For a dissector (no matter what language it's in), there are no guarantees that the full tree is built, nor should there be.</p><p>For taps and post-dissectors (which I consider to be different from dissectors; dissectors just analyze a particular protocol's packets, post-dissectors do, well, post-dissection processing of the packet summary or detail information), a way to request that particular fields be made available, or that all fields be made available, should be added if it's not already present.</p></div><div id="comment-18567-info" class="comment-info"><span class="comment-age">(12 Feb '13, 15:13)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="18572"></span><div id="comment-18572" class="comment"><div id="post-18572-score" class="comment-score"></div><div class="comment-text"><p>[replying to Guy's comment]</p><p>If you use a field extractor (ie, use Field.new() and so on), then the tap/post-dissector will get that <em>particular</em> field(s) with a call to <code>all_field_infos()</code>, because the underlying code does a hack by creating a fake tap with a fake dfilter to make it so. Well... it works except for <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6020">bug 6020</a>.<br />
</p><p>But it's definitely not the case that a tap or a post-dissector will get "all" the fields - it will get all the fields that the dissectors happened to fill, which for listener taps case is virtually none; and for post-dissectors is hit-or-miss.</p><p>I agree it should be otherwise. One way to fix this is to make the tap/post-dissector registration have a flag similar to <code>TL_REQUIRES_COLUMNS</code>, to force tree population. I.e., make both the Lua script author set such a flag, and make the C-side code use it for this purpose. That way it doesn't impact performance for anyone not needing it.</p></div><div id="comment-18572-info" class="comment-info"><span class="comment-age">(12 Feb '13, 22:10)</span> <span class="comment-user userinfo">Hadriel</span></div></div></div><div id="comment-tools-18555" class="comment-tools"></div><div class="clear"></div><div id="comment-18555-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18681"></span>

<div id="answer-container-18681" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18681-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18681-score" class="post-score" title="current number of votes">1</div><span id="post-18681-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A patch to solve this has been attached to <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6357">bug 6357</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '13, 07:47</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span> </br></p></div></div><div id="comments-container-18681" class="comments-container"></div><div id="comment-tools-18681" class="comment-tools"></div><div class="clear"></div><div id="comment-18681-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

