+++
type = "question"
title = "[closed] how to use heur_dissector_add() function to dissect."
description = '''I have put the dissector upon &quot;udp&quot;.But in the wireshark UI,open a packet,select a item, use the &quot;disscetor as&quot; option. the question is :there is no fp(my protocol) to select.why? thank U very much! follow is the code. void proto_reg_handoff_fp(void) {  mac_fdd_rach_handle = find_dissector(&quot;mac.fdd....'''
date = "2012-06-14T00:55:00Z"
lastmod = "2012-06-14T23:37:00Z"
weight = 11893
keywords = [ "fp", "heur_dissector_add" ]
aliases = [ "/questions/11893" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] how to use heur\_dissector\_add() function to dissect.](/questions/11893/how-to-use-heur_dissector_add-function-to-dissect)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11893-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11893-score" class="post-score" title="current number of votes">0</div><span id="post-11893-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have put the dissector upon "udp".But in the wireshark UI,open a packet,select a item, use the "disscetor as" option. the question is :there is no fp(my protocol) to select.why? thank U very much! follow is the code.</p><p>void proto_reg_handoff_fp(void) { mac_fdd_rach_handle = find_dissector("mac.fdd.rach"); mac_fdd_fach_handle = find_dissector("mac.fdd.fach"); mac_fdd_pch_handle = find_dissector("mac.fdd.pch"); mac_fdd_dch_handle = find_dissector("mac.fdd.dch"); mac_fdd_edch_handle = find_dissector("mac.fdd.edch"); mac_fdd_hsdsch_handle = find_dissector("mac.fdd.hsdsch"); heur_dissector_add("udp", heur_dissect_fp, proto_fp); }</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fp" rel="tag" title="see questions tagged &#39;fp&#39;">fp</span> <span class="post-tag tag-link-heur_dissector_add" rel="tag" title="see questions tagged &#39;heur_dissector_add&#39;">heur_dissector_add</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jun '12, 00:55</strong></p><img src="https://secure.gravatar.com/avatar/f6eeed42d5aadabfed2ca2cb1faabff1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smilezuzu&#39;s gravatar image" /><p><span>smilezuzu</span><br />
<span class="score" title="20 reputation points">20</span><span title="32 badges"><span class="badge1">●</span><span class="badgecount">32</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smilezuzu has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> closed <strong>14 Jun '12, 23:37</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-11893" class="comments-container"><span id="11920"></span><div id="comment-11920" class="comment"><div id="post-11920-score" class="comment-score"></div><div class="comment-text"><p><a href="http://ask.wireshark.org/questions/11913/how-to-use-umts-fp-dissector">duplicate 1</a>, <a href="http://ask.wireshark.org/questions/11894/how-to-use-the-two-function-heur_dissect_xx-and-heur_dissector_add">duplicate 2</a></p></div><div id="comment-11920-info" class="comment-info"><span class="comment-age">(14 Jun '12, 23:37)</span> <span class="comment-user userinfo">helloworld</span></div></div></div><div id="comment-tools-11893" class="comment-tools"></div><div class="clear"></div><div id="comment-11893-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question" by helloworld 14 Jun '12, 23:37

</div>

</div>

</div>

