+++
type = "question"
title = "VS2013: No External References for a new plugin"
description = '''I&#x27;ve written a test plugin for Wireshark. I did the following:  I followed the instructions in README.plugins I then created an Empty C++ project called foo in the Plugins folder in Solution Explorer I used Add -&amp;gt; Existing item to add the various files into the foo plugin folder, basically mimick...'''
date = "2015-11-08T14:46:00Z"
lastmod = "2015-11-09T03:08:00Z"
weight = 47416
keywords = [ "visual-studio" ]
aliases = [ "/questions/47416" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [VS2013: No External References for a new plugin](/questions/47416/vs2013-no-external-references-for-a-new-plugin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47416-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47416-score" class="post-score" title="current number of votes">0</div><span id="post-47416-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've written a test plugin for Wireshark. I did the following:</p><ol><li>I followed the instructions in README.plugins</li><li>I then created an Empty C++ project called foo in the Plugins folder in Solution Explorer</li><li>I used Add -&gt; Existing item to add the various files into the foo plugin folder, basically mimicking what was in the gryphon folder</li></ol><p>This all looked fine but Visual Studio hadn't picked up the External References, and I wasn't keen to hunt down the various include files and add them manually. What to do?</p><p>This is a rhetorical question as I've figured out the fix but it's worth documenting here.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-visual-studio" rel="tag" title="see questions tagged &#39;visual-studio&#39;">visual-studio</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '15, 14:46</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p><span>PaulOfford</span><br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-47416" class="comments-container"></div><div id="comment-tools-47416" class="comment-tools"></div><div class="clear"></div><div id="comment-47416-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47417"></span>

<div id="answer-container-47417" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47417-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47417-score" class="post-score" title="current number of votes">0</div><span id="post-47417-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="PaulOfford has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The answer is:</p><ol><li>Open CMakeList.txt in the Wireshark base directory</li><li>Edit the list of files after <em>set(PLUGIN_SRC_DIRS</em> to add your new plugin</li><li>Save</li><li>Change to the build directory</li><li>Run the cmake command to create the build files</li><li>Start VS using the Wiresahrk.sln in the build directory</li></ol><p>For me, the cmake command to create the build files was:</p><pre><code>cmake -D ENABLE_CHM_GUIDES=on -G &quot;Visual Studio 12 Win64&quot; ..\</code></pre><p>The above is described in the README.plugins file but it's in the section <em>3.2 Permanent addition</em> and I skipped over it because I wasn't writing a permanent addition.</p><p>Best regards...Paul</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '15, 14:58</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p><span>PaulOfford</span><br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-47417" class="comments-container"><span id="47424"></span><div id="comment-47424" class="comment"><div id="post-47424-score" class="comment-score"></div><div class="comment-text"><p>The correct solution is to copy CMakeListsCustom.txt.example in the root of the source tree to CMakeListsCustom.txt and edit as required.</p><p>The reason for this is that modifying the main CMakeLists.txt will change a git controlled file, so you'll always have to manage a merge when you update from the Wireshark repository. Using the custom file avoids this.</p><p>There is provision for similar CMakeListsCustom.txt files in the epan and ui\gtk directories.</p></div><div id="comment-47424-info" class="comment-info"><span class="comment-age">(09 Nov '15, 02:51)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="47425"></span><div id="comment-47425" class="comment"><div id="post-47425-score" class="comment-score"></div><div class="comment-text"><p>Thanks Graham. That sounds a much better solution.</p></div><div id="comment-47425-info" class="comment-info"><span class="comment-age">(09 Nov '15, 03:08)</span> <span class="comment-user userinfo">PaulOfford</span></div></div></div><div id="comment-tools-47417" class="comment-tools"></div><div class="clear"></div><div id="comment-47417-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

