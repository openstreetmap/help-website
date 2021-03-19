+++
type = "question"
title = "Lua: Add ProtoFields to Proto from within a Dissector"
description = '''Hi Folks, I am writing a dissector in Lua for a protocol which consists of arbitrary key/value pairs. I would like to generate the protocol fields on the fly by adding each unique key as it is encountered in the payload. For example, if a message contained &quot;User=Joe;Region=Europe;SpecialVar=12345&quot;, ...'''
date = "2016-08-11T15:01:00Z"
lastmod = "2016-08-11T15:01:00Z"
weight = 54761
keywords = [ "lua", "protofields", "dissector", "protocol", "protofield" ]
aliases = [ "/questions/54761" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Lua: Add ProtoFields to Proto from within a Dissector](/questions/54761/lua-add-protofields-to-proto-from-within-a-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54761-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Folks,</p><p>I am writing a dissector in Lua for a protocol which consists of arbitrary key/value pairs. I would like to generate the protocol fields on the fly by adding each unique key as it is encountered in the payload. For example, if a message contained "User=Joe;Region=Europe;SpecialVar=12345", then I would want to add User, Region and SpecialVar to the table of ProtoFields for the protocol.</p><p>Currently, I am trying to do this from within the dissector by getting the table of ProtoFields using protocolName.fields, inserting the new field, and then assigning the table back to protocolName.fields. However, when I run this code, Wireshark just hangs.<br />
</p><p>Should this be working? Or is modifying a Protocol from within its Dissector unsupported?</p><p>Note that I originally tried adding the new Protofield in place (i.e.: table.insert(protocolName.fields, newProtoField) ), but this simply did not work. So I am guessing that proto.fields returns a copy of the table as opposed to a reference (someone correct me if I am wrong).</p><p>Thanks in advance, Ryan</p></div><div id="question-tags" class="tags-container tags">lua protofields dissector protocol protofield</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Aug '16, 15:01</strong></p><img src="https://secure.gravatar.com/avatar/ba1199f4d360c53a6cc8aa6aa5da37c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ryber&#39;s gravatar image" /><p>ryber<br />
<span class="score" title="146 reputation points">146</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ryber has one accepted answer">16%</span> </br></p></div></div><div id="comments-container-54761" class="comments-container"><span id="54766"></span><div id="comment-54766" class="comment"><div id="post-54766-score" class="comment-score"></div><div class="comment-text"><p>Check <a href="https://ask.wireshark.org/questions/54620/is-there-a-way-to-give-dynamic-names-to-protocol-attributes">this question</a>.</p></div><div id="comment-54766-info" class="comment-info"><span class="comment-age">(12 Aug '16, 01:29)</span> sindy</div></div><span id="54815"></span><div id="comment-54815" class="comment"><div id="post-54815-score" class="comment-score"></div><div class="comment-text"><p>Thanks, Sindy. That question represents the same problem I am trying to solve. Your suggestions had occurred to me as a workaround, but I was hoping to be able to do it "properly".</p></div><div id="comment-54815-info" class="comment-info"><span class="comment-age">(15 Aug '16, 05:29)</span> ryber</div></div><span id="54817"></span><div id="comment-54817" class="comment"><div id="post-54817-score" class="comment-score">1</div><div class="comment-text"><p>There is no "proper" solution of this, given the overall architecture. The clear distinction between registration and execution phase has its purpose - all protocol fields can be used for display filter, so they must be known before the actual dissection takes place. Otherwise it e.g. wouldn't be possible to make a formal check of the display filter expression.</p><p>So in your case, if you know the complete set of possible field names, you can register all of them in advance and only practically use the ones which actually arrive in a frame, but if the names are totally unpredictable, only the "workaround" can be used.</p></div><div id="comment-54817-info" class="comment-info"><span class="comment-age">(15 Aug '16, 05:37)</span> sindy</div></div></div><div id="comment-tools-54761" class="comment-tools"></div><div class="clear"></div><div id="comment-54761-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

