+++
type = "question"
title = "Wireshark Crash when FTYPE_LOOKUP is Called for one of the Packets"
description = '''I was writing a Custom Wireshark Dissector. But when I ran the plugin I created, by choosing packets to be Decoded as my protocol, Wireshark Crashes with Error that &quot;Application has requested runtime to terminate it in an unusual Way&quot;. To Debug it further I added printf statements and also ran Wires...'''
date = "2011-06-18T14:02:00Z"
lastmod = "2011-06-19T10:03:00Z"
weight = 4617
keywords = [ "crash", "wireshark" ]
aliases = [ "/questions/4617" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Crash when FTYPE\_LOOKUP is Called for one of the Packets](/questions/4617/wireshark-crash-when-ftype_lookup-is-called-for-one-of-the-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4617-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4617-score" class="post-score" title="current number of votes">0</div><span id="post-4617-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was writing a Custom Wireshark Dissector. But when I ran the plugin I created, by choosing packets to be Decoded as my protocol, Wireshark Crashes with Error that "Application has requested runtime to terminate it in an unusual Way".<br />
To Debug it further I added printf statements and also ran Wireshark from Visual C++ 2008 EE in Debug Mode(by adding breakpoints). What i see is that for one of the Packets the crash occurs when I call FTYPE_LOOKUP while a call to proto_tree_add_item is made for Length Field(4 bytes) of the Protocol.<br />
From within proto_tree_add_item(), function alloc_field_info() is Called. From here get_hfi_and_length() is called which gives hfinfo(or header field info). This hfinfo is passed to new_field_info() function and this hfinfo is assigned to hfinfo field of field_info structure inside this function. The hfinfo-&gt;type is passed then to fvalue_init(). Here FTYPE_LOOKUP(Defined in ftypes.c) is Called where it crashes.<br />
<strong>This is maybe because the type is not correct. I see hfinfo structure having junk values. It seems PROTO_REGISTRAR_GET_NTH. Why so ? Is there some problem in the way I have registered hf array ?</strong> <strong>Kindly note nothing abnormal happens if same code is called for other Packets.</strong></p><p><em>This is how I have registered hf array</em><br />
proto_register_field_array(proto, hf_base, array_length(hf_base));</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jun '11, 14:02</strong></p><img src="https://secure.gravatar.com/avatar/98b912fc4a13fff8fae6632b403d9ce6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="varun%20saxena&#39;s gravatar image" /><p><span>varun saxena</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="varun saxena has one accepted answer">100%</span> </br></br></p></div></div><div id="comments-container-4617" class="comments-container"><span id="4618"></span><div id="comment-4618" class="comment"><div id="post-4618-score" class="comment-score"></div><div class="comment-text"><p><strong>I meant it seems PROTO_REGISTRAR_GET_NTH() does not give me correct hfinfo structure. What am I doing wrong ?</strong></p></div><div id="comment-4618-info" class="comment-info"><span class="comment-age">(18 Jun '11, 14:04)</span> <span class="comment-user userinfo">varun saxena</span></div></div></div><div id="comment-tools-4617" class="comment-tools"></div><div class="clear"></div><div id="comment-4617-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4621"></span>

<div id="answer-container-4621" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4621-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4621-score" class="post-score" title="current number of votes">0</div><span id="post-4621-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SYN-bit has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Problem Resolved. I had not defined the Hfinfo Array as static</p></div><div class="answer-controls post-controls"><div class="community-wiki">This answer is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '11, 10:03</strong></p><img src="https://secure.gravatar.com/avatar/98b912fc4a13fff8fae6632b403d9ce6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="varun%20saxena&#39;s gravatar image" /><p><span>varun saxena</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="varun saxena has one accepted answer">100%</span> </br></br></p></div></div><div id="comments-container-4621" class="comments-container"></div><div id="comment-tools-4621" class="comment-tools"></div><div class="clear"></div><div id="comment-4621-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

