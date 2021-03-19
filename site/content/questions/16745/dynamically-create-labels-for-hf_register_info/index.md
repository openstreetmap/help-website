+++
type = "question"
title = "Dynamically create labels for hf_register_info"
description = '''Hi Forum I have a protocol that I am dissecting and I have been creating and registering each field in a hf_register_info to get the correct labels X00001 and X00002 etc for the fields.  Data (1000 entries) X0001: 0001 X0002: 4525  static hf_register_info hf[] = {  { &amp;amp;hf_X00001,  { &quot;X00001&quot;, &quot;FO...'''
date = "2012-12-10T03:13:00Z"
lastmod = "2012-12-10T08:22:00Z"
weight = 16745
keywords = [ "hf_register_info", "records" ]
aliases = [ "/questions/16745" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Dynamically create labels for hf\_register\_info](/questions/16745/dynamically-create-labels-for-hf_register_info)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16745-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16745-score" class="post-score" title="current number of votes">0</div><span id="post-16745-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Forum</p><p>I have a protocol that I am dissecting and I have been creating and registering each field in a hf_register_info to get the correct labels X00001 and X00002 etc for the fields.</p><ul><li>Data (1000 entries) X0001: 0001 X0002: 4525</li></ul><p>static hf_register_info hf[] = { { &amp;hf_X00001, { "X00001", "FOO.X00001", FT_UINT16, BASE_DEC, NULL, 0x0,NULL, HFILL } }, ... { &amp;hf_X99999, { "X99999", "FOO.X99999", FT_UINT16, BASE_DEC, NULL, 0x0,NULL, HFILL } } }</p><p>In reality the only item that is changing is the label prefix being showing in the dissection. I don't need to be able to search using F00.X00001.</p><p>Is there anyway to dynamically create this prefix label to avoid having to create massive hf_register_info records??? Ideally without the need for the hf_register_info record at all.</p><p>This is becoming a massive list of names and there must be something I am missing.</p><p>Thanks</p><p>Stuart</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-hf_register_info" rel="tag" title="see questions tagged &#39;hf_register_info&#39;">hf_register_info</span> <span class="post-tag tag-link-records" rel="tag" title="see questions tagged &#39;records&#39;">records</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Dec '12, 03:13</strong></p><img src="https://secure.gravatar.com/avatar/e12bbe1b488f2a19cdf565465e260d19?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="StuieNorris&#39;s gravatar image" /><p><span>StuieNorris</span><br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="StuieNorris has no accepted answers">0%</span></p></div></div><div id="comments-container-16745" class="comments-container"></div><div id="comment-tools-16745" class="comment-tools"></div><div class="clear"></div><div id="comment-16745-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="16748"></span>

<div id="answer-container-16748" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16748-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16748-score" class="post-score" title="current number of votes">0</div><span id="post-16748-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, you're going to have to create all those hf entries at some point. You could dynamically generate the table, maybe even combining some static entries with some dynamically-created ones. packet-diameter.c does this for example: there are some static entries for basic stuff and then the rest of the entries come from reading the Diameter XML files; these are combined before registering the whole table.</p><p>You could also create lots of smaller arrays and register them all in a loop (packet-tpncp.c does this) but I the the first solution would be easier.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Dec '12, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-16748" class="comments-container"></div><div id="comment-tools-16748" class="comment-tools"></div><div class="clear"></div><div id="comment-16748-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16749"></span>

<div id="answer-container-16749" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16749-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16749-score" class="post-score" title="current number of votes">0</div><span id="post-16749-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Another possibility:</p><p>If you really don't need to filter on the specific fields, then I think the following will work.</p><ol><li>Create 1 generic hf[] entry for the field;</li><li>Use proto_tree_add_uint_format(...) to specify the info displayed (including the label) for the field.</li></ol><p>If you do this, then I think you can generate the label name programattically when doing the proto_tree_add_uint() so that you can use a simple loop to display the data.</p><p>This approach does allow searching all of the fields.</p><p>Yet another possibility (less favored): proto_tree_add_text(...); no hf[] entry req'd; cannot be searched.</p><p>See doc/README.developer ....</p><hr /><p>proto_tree_add_uint(...) ...</p><p>These routines are used to add items to the protocol tree when the dissector routine wants complete control over how the field and value will be represented on the GUI tree. The argument giving the value is the same as the corresponding proto_tree_add_XXX() function; the rest of the arguments are a "printf"-style format and any arguments for that format. The caller must include the name of the field in the format; it is not added automatically as in the proto_tree_add_XXX() functions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Dec '12, 08:22</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Dec '12, 08:26</strong> </span></p></div></div><div id="comments-container-16749" class="comments-container"></div><div id="comment-tools-16749" class="comment-tools"></div><div class="clear"></div><div id="comment-16749-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

