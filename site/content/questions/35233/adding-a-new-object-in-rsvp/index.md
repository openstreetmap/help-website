+++
type = "question"
title = "Adding a new object in rsvp"
description = '''I want to add a new object type in packet-rsvp.c. As i saw i have to add it in enum rsvp_classes according to its C-Num and also add it in value_string rsvp_class_vals[]. I&#x27; m not quite sure what should be done with: rsvp_class_to_filter_num (int classnum) {} should i just add a new filter with the ...'''
date = "2014-08-05T12:33:00Z"
lastmod = "2014-08-05T12:33:00Z"
weight = 35233
keywords = [ "add", "object", "rsvp" ]
aliases = [ "/questions/35233" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Adding a new object in rsvp](/questions/35233/adding-a-new-object-in-rsvp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35233-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35233-score" class="post-score" title="current number of votes">0</div><span id="post-35233-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to add a new object type in packet-rsvp.c. As i saw i have to add it in enum rsvp_classes according to its C-Num and also add it in value_string rsvp_class_vals[]. I' m not quite sure what should be done with:<br />
<strong>rsvp_class_to_filter_num (int classnum) {}</strong> should i just add a new filter with the object's name according to its C-Num? and <strong>rsvp_class_to_tree_type (int classnum) {}</strong> i don't understand the use of tree types "TT_ObjectName", what if i add another TT_ObjectName with a new object in tree types list enum? Should i add it at the end?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-add" rel="tag" title="see questions tagged &#39;add&#39;">add</span> <span class="post-tag tag-link-object" rel="tag" title="see questions tagged &#39;object&#39;">object</span> <span class="post-tag tag-link-rsvp" rel="tag" title="see questions tagged &#39;rsvp&#39;">rsvp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '14, 12:33</strong></p><img src="https://secure.gravatar.com/avatar/8ee003c9042bb54a75a39046704e8d5d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Miltos%20Patsiouras&#39;s gravatar image" /><p><span>Miltos Patsi...</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Miltos Patsiouras has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-35233" class="comments-container"></div><div id="comment-tools-35233" class="comment-tools"></div><div class="clear"></div><div id="comment-35233-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

