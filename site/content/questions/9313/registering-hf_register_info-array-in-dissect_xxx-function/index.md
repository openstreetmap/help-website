+++
type = "question"
title = "registering hf_register_info array in dissect_XXX function"
description = '''Hi, Is it a good practice to register some entries of hf_register_info array from dissect_XXX function instead of proto_register_XXX() function. Reason being : the value_string structure assigned to some fields(through vals() function) changes based on the data fetched from packet in dissector code....'''
date = "2012-03-02T10:24:00Z"
lastmod = "2012-03-06T06:50:00Z"
weight = 9313
keywords = [ "development", "dissector", "proto_register" ]
aliases = [ "/questions/9313" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [registering hf\_register\_info array in dissect\_XXX function](/questions/9313/registering-hf_register_info-array-in-dissect_xxx-function)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9313-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9313-score" class="post-score" title="current number of votes">0</div><span id="post-9313-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Is it a good practice to register some entries of hf_register_info array from dissect_XXX function instead of proto_register_XXX() function.</p><p>Reason being : the value_string structure assigned to some fields(through vals() function) changes based on the data fetched from packet in dissector code. Basically I have a requirement where the same field and with the same value will be assigned different names based on some data part of packet.</p><p>Looking for your help..Thanks in advance :)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-proto_register" rel="tag" title="see questions tagged &#39;proto_register&#39;">proto_register</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Mar '12, 10:24</strong></p><img src="https://secure.gravatar.com/avatar/d221d26845724614e25ab8e51887c4bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ashish_goel&#39;s gravatar image" /><p><span>ashish_goel</span><br />
<span class="score" title="15 reputation points">15</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ashish_goel has no accepted answers">0%</span></p></div></div><div id="comments-container-9313" class="comments-container"></div><div id="comment-tools-9313" class="comment-tools"></div><div class="clear"></div><div id="comment-9313-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9367"></span>

<div id="answer-container-9367" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9367-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9367-score" class="post-score" title="current number of votes">0</div><span id="post-9367-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The normal approach for this kind of thing is to just register all the possible hf's you might need. So: it is not good practice to register them in the dissect_XXX() function.</p><p>There are times when it's truly not possible to register them all ahead of time; I'm thinking of, for example, the MATE plugin: the hf's it needs depend on the configuration file. IIRC it does some kind of delayed initialization. But I'm pretty sure it's still done before dissection begins.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '12, 11:15</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-9367" class="comments-container"><span id="9376"></span><div id="comment-9376" class="comment"><div id="post-9376-score" class="comment-score"></div><div class="comment-text"><p>can you elaborate a more on the delayed initialization part?? How it is done before dissection??</p></div><div id="comment-9376-info" class="comment-info"><span class="comment-age">(05 Mar '12, 19:09)</span> <span class="comment-user userinfo">ashish_goel</span></div></div><span id="9395"></span><div id="comment-9395" class="comment"><div id="post-9395-score" class="comment-score"></div><div class="comment-text"><p>Actually I'm not too sure: I just know (well, I'm pretty sure anyway) that the MATE plugin can't register it's hf_ entries until it has read its configuration file which means it ends up regitering the hf_ entries "late." But I could be wrong about that. If you're really interested, I'd suggest studying how MATE does it.</p></div><div id="comment-9395-info" class="comment-info"><span class="comment-age">(06 Mar '12, 06:50)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-9367" class="comment-tools"></div><div class="clear"></div><div id="comment-9367-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

