+++
type = "question"
title = "Get Wireshark Install Directory inside Dissector"
description = '''How can I get the Wireshark install directory from within a wireshark dissector? My dissector relies on some external libraries and I would like to avoid hard coding &quot;C:Program FilesWiresharkPluginsFooDebendancies&quot; Thank you for your time, Brandon'''
date = "2011-07-25T08:09:00Z"
lastmod = "2011-07-26T13:24:00Z"
weight = 5223
keywords = [ "directory", "dissector", "library", "install", "dll" ]
aliases = [ "/questions/5223" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Get Wireshark Install Directory inside Dissector](/questions/5223/get-wireshark-install-directory-inside-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5223-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5223-score" class="post-score" title="current number of votes">0</div><span id="post-5223-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I get the Wireshark install directory from within a wireshark dissector? My dissector relies on some external libraries and I would like to avoid hard coding "C:Program FilesWiresharkPluginsFooDebendancies"</p><p>Thank you for your time, Brandon</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-directory" rel="tag" title="see questions tagged &#39;directory&#39;">directory</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-library" rel="tag" title="see questions tagged &#39;library&#39;">library</span> <span class="post-tag tag-link-install" rel="tag" title="see questions tagged &#39;install&#39;">install</span> <span class="post-tag tag-link-dll" rel="tag" title="see questions tagged &#39;dll&#39;">dll</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jul '11, 08:09</strong></p><img src="https://secure.gravatar.com/avatar/b65eb296474b8a4c664c8f7bc0ba2234?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="officialhopsof&#39;s gravatar image" /><p><span>officialhopsof</span><br />
<span class="score" title="31 reputation points">31</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="officialhopsof has 2 accepted answers">100%</span></p></div></div><div id="comments-container-5223" class="comments-container"></div><div id="comment-tools-5223" class="comment-tools"></div><div class="clear"></div><div id="comment-5223-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5233"></span>

<div id="answer-container-5233" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5233-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5233-score" class="post-score" title="current number of votes">1</div><span id="post-5233-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="officialhopsof has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use one of the routines in epan/filesystem.c, for example get_plugin_dir().</p><p>Not that you should normally be doing any such thing in a dissector...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jul '11, 14:05</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-5233" class="comments-container"><span id="5279"></span><div id="comment-5279" class="comment"><div id="post-5279-score" class="comment-score"></div><div class="comment-text"><h1 id="include-epanfilesystem.c">include &lt;epan/filesystem.c&gt;<br />
</h1><p>Causes linker errors, specifically:<br />
error LNK2019: unresolved external symbol _ws_stdio_stat64 referenced in function _test_for_directory<br />
error LNK2019: unresolved external symbol _utf_16to8 referenced in function _init_progfile_dir<br />
error LNK2019: unresolved external symbol _getenv_utf8 referenced in function _get_datafile_dir<br />
error LNK2019: unresolved external symbol _ws_stdio_remove referenced in function _delete_directory<br />
error LNK2019: unresolved external symbol _ws_stdio_rename referenced in function _rename_persconffile_profile</p></div><div id="comment-5279-info" class="comment-info"><span class="comment-age">(26 Jul '11, 12:56)</span> <span class="comment-user userinfo">officialhopsof</span></div></div><span id="5280"></span><div id="comment-5280" class="comment"><div id="post-5280-score" class="comment-score"></div><div class="comment-text"><p>error LNK2019: unresolved external symbol _ws_stdio_mkdir referenced in function _create_persconffile_profile<br />
packet-vmf.obj : error LNK2019: unresolved external symbol <strong>imp</strong><span class="__cf_email__" data-cfemail="eab9a2ad8f9eb99a8f89838b86ac85868e8f98ba8b9e82bdaadbdc">[email protected]</span> referenced in function _get_persdatafile_dir<br />
error LNK2019: unresolved external symbol _ws_stdio_unlink referenced in function _deletefile<br />
error LNK2019: unresolved external symbol _ws_stdio_open referenced in function _copy_file_binary_mode<br />
</p><p>But this appears like it's what I want.</p></div><div id="comment-5280-info" class="comment-info"><span class="comment-age">(26 Jul '11, 12:56)</span> <span class="comment-user userinfo">officialhopsof</span></div></div><span id="5281"></span><div id="comment-5281" class="comment"><div id="post-5281-score" class="comment-score"></div><div class="comment-text"><p>It's an atrocity to <code>#include</code> a C file. Include the <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/filesystem.h?revision=36077&amp;view=markup#l55">header</a> instead.</p></div><div id="comment-5281-info" class="comment-info"><span class="comment-age">(26 Jul '11, 13:03)</span> <span class="comment-user userinfo">bstn</span></div></div><span id="5283"></span><div id="comment-5283" class="comment"><div id="post-5283-score" class="comment-score"></div><div class="comment-text"><p>Oh! That was a typo I didn't spot! Thanks!</p></div><div id="comment-5283-info" class="comment-info"><span class="comment-age">(26 Jul '11, 13:24)</span> <span class="comment-user userinfo">officialhopsof</span></div></div></div><div id="comment-tools-5233" class="comment-tools"></div><div class="clear"></div><div id="comment-5233-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

