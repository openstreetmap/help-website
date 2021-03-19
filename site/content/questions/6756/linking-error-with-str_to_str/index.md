+++
type = "question"
title = "Linking Error with str_to_str"
description = '''I&#x27;ve made a custom dissector plugin for Wireshark and have a weird linking error. This is my first plugin and am using MSVC 2010 express as my compiler.  I get a linking error that it can&#x27;t resolve the str_to_str function in value_string.h. It states &quot;unresolved external symbol _str_to_str reference...'''
date = "2011-10-06T13:04:00Z"
lastmod = "2011-10-07T11:21:00Z"
weight = 6756
keywords = [ "compile", "development", "dissector", "linker" ]
aliases = [ "/questions/6756" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Linking Error with str\_to\_str](/questions/6756/linking-error-with-str_to_str)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6756-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6756-score" class="post-score" title="current number of votes">1</div><span id="post-6756-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've made a custom dissector plugin for Wireshark and have a weird linking error. This is my first plugin and am using MSVC 2010 express as my compiler.<br />
</p><p>I get a linking error that it can't resolve the str_to_str function in value_string.h. It states "unresolved external symbol _str_to_str referenced in function xyz". I'm using value_string and string_string structs and have no problem compiling and linking other functions in the header (such as val_to_str).</p><p>any thoughts or ideas why only some things in the header get linked?</p><p>BTW also had this happen with the tvb_get_bits from tvbuff.h as well...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-compile" rel="tag" title="see questions tagged &#39;compile&#39;">compile</span> <span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-linker" rel="tag" title="see questions tagged &#39;linker&#39;">linker</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Oct '11, 13:04</strong></p><img src="https://secure.gravatar.com/avatar/5b7bc5ccd49bd6306eb7b670bbc42300?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="redraymon&#39;s gravatar image" /><p><span>redraymon</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="redraymon has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Oct '11, 13:05</strong> </span></p></div></div><div id="comments-container-6756" class="comments-container"><span id="6757"></span><div id="comment-6757" class="comment"><div id="post-6757-score" class="comment-score"></div><div class="comment-text"><p>Does the error remain if you use MSVC2008 (EE is fine) in stead? Last I checked, 2008 is still the Windows toolchain used for official builds.</p></div><div id="comment-6757-info" class="comment-info"><span class="comment-age">(06 Oct '11, 13:12)</span> <span class="comment-user userinfo">multipleinte...</span></div></div><span id="6759"></span><div id="comment-6759" class="comment"><div id="post-6759-score" class="comment-score"></div><div class="comment-text"><p>Haven't tried with 2008. Don't have a copy and haven't looked for it. If it hinders me then I may try that road but I've built the dissector and essentially have worked around these two functions.</p><p>Just found it odd that it would not recognize one function but would be fine with other functions in the same header.</p></div><div id="comment-6759-info" class="comment-info"><span class="comment-age">(06 Oct '11, 13:16)</span> <span class="comment-user userinfo">redraymon</span></div></div><span id="6761"></span><div id="comment-6761" class="comment"><div id="post-6761-score" class="comment-score"></div><div class="comment-text"><p>Are you building your dissector as part of the core Wireshark or a plugin? If you are building it as a plugin, have you compiled Wireshark at least once? Furthermore, are you <em>sure</em> that you are compiling using the correct CRT? MSVC2010 defaults to <code>v100</code>, but official versions of Wireshark (e.g. from the <a href="http://www.wireshark.org/download.html">Downloads</a> page) currently uses <code>v90</code>.</p></div><div id="comment-6761-info" class="comment-info"><span class="comment-age">(06 Oct '11, 13:53)</span> <span class="comment-user userinfo">multipleinte...</span></div></div><span id="6782"></span><div id="comment-6782" class="comment"><div id="post-6782-score" class="comment-score"></div><div class="comment-text"><p>Building it as a plugin. I'm using v100 and everything compiles and runs correctly, unless I try to use this one function.</p><p>I know that it isn't the same CRT but I'm unsure of why certain functions from a header file would link when one or two don't.</p></div><div id="comment-6782-info" class="comment-info"><span class="comment-age">(07 Oct '11, 06:16)</span> <span class="comment-user userinfo">redraymon</span></div></div></div><div id="comment-tools-6756" class="comment-tools"></div><div class="clear"></div><div id="comment-6756-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6771"></span>

<div id="answer-container-6771" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6771-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6771-score" class="post-score" title="current number of votes">2</div><span id="post-6771-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="redraymon has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The symbol needs to be exported from libwireshark. Edit epan\libwireshark.def and add an entry for <code>str_to_str</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '11, 01:05</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Oct '11, 01:16</strong> </span></p></div></div><div id="comments-container-6771" class="comments-container"><span id="6783"></span><div id="comment-6783" class="comment"><div id="post-6783-score" class="comment-score"></div><div class="comment-text"><p>I'll give this a try and see what I find out.</p></div><div id="comment-6783-info" class="comment-info"><span class="comment-age">(07 Oct '11, 06:16)</span> <span class="comment-user userinfo">redraymon</span></div></div><span id="6785"></span><div id="comment-6785" class="comment"><div id="post-6785-score" class="comment-score"></div><div class="comment-text"><p>Add the function to the libwireshark.def file and recompiled wireshark. Recompiled my plugin with no issues but trying to run the release version with it fails.</p><p>Seems that the official release wasn't compiled with this function either... should this be suggested as a bug? New to this, how is that done?</p></div><div id="comment-6785-info" class="comment-info"><span class="comment-age">(07 Oct '11, 06:40)</span> <span class="comment-user userinfo">redraymon</span></div></div><span id="6786"></span><div id="comment-6786" class="comment"><div id="post-6786-score" class="comment-score"></div><div class="comment-text"><p>Normally opening a bug on https://bugs.wireshark.org is the way to go, but I just committed the change in rev 39304 so there's no need.</p><p>BTW, tvb_get_bits is already exported in trunk.</p><p>I scheduled both 39304 (str_to_str) and 38301 (tvb_get_bits) to be backported to 1.6.3.</p></div><div id="comment-6786-info" class="comment-info"><span class="comment-age">(07 Oct '11, 07:00)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="6787"></span><div id="comment-6787" class="comment"><div id="post-6787-score" class="comment-score"></div><div class="comment-text"><p>If the answer is good, please mark it as so by checking it.</p></div><div id="comment-6787-info" class="comment-info"><span class="comment-age">(07 Oct '11, 07:07)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="6792"></span><div id="comment-6792" class="comment"><div id="post-6792-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the help!</p></div><div id="comment-6792-info" class="comment-info"><span class="comment-age">(07 Oct '11, 11:21)</span> <span class="comment-user userinfo">redraymon</span></div></div></div><div id="comment-tools-6771" class="comment-tools"></div><div class="clear"></div><div id="comment-6771-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

