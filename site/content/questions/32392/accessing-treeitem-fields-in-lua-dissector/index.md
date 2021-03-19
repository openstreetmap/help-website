+++
type = "question"
title = "Accessing TreeItem fields in LUA dissector"
description = '''Hello, I&#x27;m writing a LUA dissector, and I have it basically working (the tree shows OK in Wireshark). Now I would like to add into the &quot;Info&quot; column some information that I have already parsed, and that I have already added to my tree. The problem is that I&#x27;m using some ProtoFields in order to extra...'''
date = "2014-05-02T06:27:00Z"
lastmod = "2014-05-05T00:20:00Z"
weight = 32392
keywords = [ "lua", "protofields", "treeitem", "fields" ]
aliases = [ "/questions/32392" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Accessing TreeItem fields in LUA dissector](/questions/32392/accessing-treeitem-fields-in-lua-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32392-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32392-score" class="post-score" title="current number of votes">0</div><span id="post-32392-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm writing a LUA dissector, and I have it basically working (the tree shows OK in Wireshark). Now I would like to add into the "Info" column some information that I have already parsed, and that I have already added to my tree.</p><p>The problem is that I'm using some ProtoFields in order to extract information from the buffer and to populate my tree. Unfortunately I read that there is no way to use ProtoFields to extract information storing it into locals, and that the only purpose they can be used for is passing them to "add" (or "add_le" in my case) TreeItem's methods.. that is what I'm doing in fact.. (is this right?).</p><p>For this reason, I'm wondering whether is there any method to extract information fields from the tree itself (after I got them added to the tree by using "add_le" and the protofield).</p><p>Does it ?</p><p>I know I could re-parse the buffer and re-extract information without using ProtoField in order to be able to store my information in locals, but indeed what I would like to do is exactly trying to avoid this "duplicated parsing"...</p><p>Thanks Andrea</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-protofields" rel="tag" title="see questions tagged &#39;protofields&#39;">protofields</span> <span class="post-tag tag-link-treeitem" rel="tag" title="see questions tagged &#39;treeitem&#39;">treeitem</span> <span class="post-tag tag-link-fields" rel="tag" title="see questions tagged &#39;fields&#39;">fields</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 May '14, 06:27</strong></p><img src="https://secure.gravatar.com/avatar/96076cb0346f60280e33f1964e316475?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andrea&#39;s gravatar image" /><p><span>Andrea</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andrea has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 May '14, 11:48</strong> </span></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span></p></div></div><div id="comments-container-32392" class="comments-container"></div><div id="comment-tools-32392" class="comment-tools"></div><div class="clear"></div><div id="comment-32392-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32436"></span>

<div id="answer-container-32436" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32436-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32436-score" class="post-score" title="current number of votes">2</div><span id="post-32436-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Unfortunately I read that there is no way to use ProtoFields to extract information storing it into locals, and that the only purpose they can be used for is passing them to "add" (or "add_le" in my case) TreeItem's methods.</p></blockquote><p>Not true - well... I should say that's not the whole story. A <code>ProtoField</code> is really just metadata about a new field you created for your <code>Protocol</code>, as opposed to using an already existing field. When you pass a <code>ProtoField</code> as an argument into "<code>TreeItem:add()</code>" (or "<code>add_le()</code>"), you're telling Wireshark to use that metadata to extract/parse information from the passed-in <code>TvbRange</code> argument (or to use a raw value if you gave a value argument instead of a <code>TvbRange</code>). The "<code>TreeItem:add()</code>" function does that parsing of the <code>TvbRange</code>, per the info in the <code>ProtoField</code> metadata, and adds the parsed info to the tree, etc.</p><p>There is currently only one return value for the "<code>TreeItem:add()</code>" function call, which is a created child subtree. So there isn't any way for your script to get back the parsed info to store in a local variable... not from a function call of "<code>TreeItem:add()</code>". <strong>But</strong>, the parsed info is added into Wireshark as a real field's data, so you <em>can</em> retrieve it using the normal <code>Field</code> and <code>FieldInfo</code> mechanism, <em>after</em> the call to "<code>TreeItem:add()</code>".</p><p>This is in fact done in the tutorial dissector script - the script at the top of the <a href="http://wiki.wireshark.org/Lua/Examples">wiki Lua examples page</a>. If you download that script, you'll find there are four <code>Field</code>s which are used to retrieve information from <code>ProtoField</code>s, as follows:</p><pre><code>local questions_field       = Field.new(&quot;mydns.num_questions&quot;)
local query_type_field      = Field.new(&quot;mydns.query.type&quot;)
local query_class_field     = Field.new(&quot;mydns.query.class&quot;)
local response_field        = Field.new(&quot;mydns.flags.response&quot;)</code></pre><p>Each of those are later used during dissection, to retrieve the field data previously parsed from "<code>TreeItem:add()</code>" calls with <code>ProtoField</code>s.</p><hr /><p>I should note that this is slowly changing in release 1.11.4: the "<code>TreeItem:add_packet_field()</code>" function, which is similar to "<code>TreeItem:add()</code>", is being changed to return not only the created child subtree, but also the parsed value. This change isn't complete yet though - it only works for a couple of field types right now (time and bytes fields types).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '14, 11:46</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-32436" class="comments-container"><span id="32525"></span><div id="comment-32525" class="comment"><div id="post-32525-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your reply! It seems a nice and clean method to do what I'd like to do. I like it :)</p><p>Unfortunately this is not suitable for me, as would like to target stable wireshark releases (1.10.7 right now).. As the comment in the example script suggests, it is not possible to create a Field for a just-registered ProtoField :(</p><p>Any workaround or other suggestion while waiting for code in 1.11 to become stable?</p><p>Thank you Andrea</p></div><div id="comment-32525-info" class="comment-info"><span class="comment-age">(05 May '14, 00:20)</span> <span class="comment-user userinfo">Andrea</span></div></div></div><div id="comment-tools-32436" class="comment-tools"></div><div class="clear"></div><div id="comment-32436-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

