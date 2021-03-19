+++
type = "question"
title = "Remove update &quot;feature&quot;"
description = '''Is there a way to disable the update &quot;feature&quot; during compilation of wireshark. We&#x27;re in the middle of developing a protocol, and updating to a version that doesn&#x27;t contain the dissector is not preferable. Thanks Brian'''
date = "2013-09-16T11:26:00Z"
lastmod = "2013-09-16T14:07:00Z"
weight = 24780
keywords = [ "update", "remove", "feature" ]
aliases = [ "/questions/24780" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Remove update "feature"](/questions/24780/remove-update-feature)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24780-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24780-score" class="post-score" title="current number of votes">0</div><span id="post-24780-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to disable the update "feature" during compilation of wireshark. We're in the middle of developing a protocol, and updating to a version that doesn't contain the dissector is not preferable.</p><p>Thanks Brian</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-remove" rel="tag" title="see questions tagged &#39;remove&#39;">remove</span> <span class="post-tag tag-link-feature" rel="tag" title="see questions tagged &#39;feature&#39;">feature</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Sep '13, 11:26</strong></p><img src="https://secure.gravatar.com/avatar/ca4d08b00778143dab07e2cde30f653c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brwiese&#39;s gravatar image" /><p><span>brwiese</span><br />
<span class="score" title="26 reputation points">26</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brwiese has one accepted answer">50%</span></p></div></div><div id="comments-container-24780" class="comments-container"></div><div id="comment-tools-24780" class="comment-tools"></div><div class="clear"></div><div id="comment-24780-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24781"></span>

<div id="answer-container-24781" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24781-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24781-score" class="post-score" title="current number of votes">1</div><span id="post-24781-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In <code>epan/prefs.c:pre_init_prefs()</code>, set <code>prefs.gui_update_enabled = FALSE;</code></p><p><strong>AN UPDATE</strong></p><p>So maybe it depends on what you're trying to accomplish, but I've thought of another option as well, bringing the list to the following 3:</p><ol><li><p>If you want to disable the update feature completely, then Gerald's suggestion to comment out <code>WINSPARKLE_PKG</code> in config.nmake is the answer.</p></li><li><p>If you want to allow the users to be able to re-enable the feature, then you can use my original suggestion; however, if you do that, then updates will be based on the latest official releases, not your own releases, which may not be desirable.</p></li><li><p>If you want to be able to support automatic updates with your own customized Wireshark releases, then you should be able to modify <code>ui/software_update.c:get_appcast_update_url()</code> to point the <code>update_url_str</code> to your own update location instead of to the official one. (I actually ran a quick test of this, and it looks like it will work.)</p></li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '13, 11:38</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Sep '13, 12:06</strong> </span></p></div></div><div id="comments-container-24781" class="comments-container"><span id="24783"></span><div id="comment-24783" class="comment"><div id="post-24783-score" class="comment-score">1</div><div class="comment-text"><p>You can also disable it at compile time by commenting out <code>WINSPARKLE_PKG</code> in config.nmake.</p></div><div id="comment-24783-info" class="comment-info"><span class="comment-age">(16 Sep '13, 14:07)</span> <span class="comment-user userinfo">Gerald Combs ♦♦</span></div></div></div><div id="comment-tools-24781" class="comment-tools"></div><div class="clear"></div><div id="comment-24781-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

