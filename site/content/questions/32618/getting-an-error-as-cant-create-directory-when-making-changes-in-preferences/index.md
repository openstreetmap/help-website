+++
type = "question"
title = "Getting an error as Can&#x27;t create directory when making changes in preferences."
description = '''I am using Wireshark 1.10.7, whenever I make any changes in preferences and click Apply/Ok, I am getting the follow error &quot;Can&#x27;t create directory &quot;C:&#92;Users&#92;Admin&#92;Application Data&#92;Wireshark&quot; for preferences file: File exists. I tried uninstalling and removing all the registry file related to Wireshar...'''
date = "2014-05-07T13:52:00Z"
lastmod = "2014-05-09T15:19:00Z"
weight = 32618
keywords = [ "preferences" ]
aliases = [ "/questions/32618" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Getting an error as Can't create directory when making changes in preferences.](/questions/32618/getting-an-error-as-cant-create-directory-when-making-changes-in-preferences)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32618-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32618-score" class="post-score" title="current number of votes">0</div><span id="post-32618-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using Wireshark 1.10.7, whenever I make any changes in preferences and click Apply/Ok, I am getting the follow error "Can't create directory "C:\Users\Admin\Application Data\Wireshark" for preferences file: File exists.</p><p>I tried uninstalling and removing all the registry file related to Wireshark and install it again, still hte issue persist. I also removed the wireshark folder from AppData\Roaming folder that didn't help either.</p><p>Please Help me resolve this issue.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-preferences" rel="tag" title="see questions tagged &#39;preferences&#39;">preferences</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 May '14, 13:52</strong></p><img src="https://secure.gravatar.com/avatar/01086bd9f5acb710a4f58ed11d2c68be?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="prashant4uall&#39;s gravatar image" /><p><span>prashant4uall</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="prashant4uall has no accepted answers">0%</span></p></div></div><div id="comments-container-32618" class="comments-container"></div><div id="comment-tools-32618" class="comment-tools"></div><div class="clear"></div><div id="comment-32618-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32671"></span>

<div id="answer-container-32671" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32671-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32671-score" class="post-score" title="current number of votes">0</div><span id="post-32671-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>"Can't create directory "C:\Users\Admin\Application Data\Wireshark" for preferences file: File exists.</p></blockquote><p>That sounds like a Windows file permission problem. Please check the permissions of C:\Users\Admin\Application Data\Wireshark.</p><p>To verify the problem: Open the preferences file in an editor. Modify something and then try to save it.</p><p>If you get the same error: Check your file permissions (see above).<br />
</p><p>If you don't get the error: Please tell us how you started Wireshark, as then it apparently is running within a different user context.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '14, 11:06</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 May '14, 11:06</strong> </span></p></div></div><div id="comments-container-32671" class="comments-container"><span id="32685"></span><div id="comment-32685" class="comment"><div id="post-32685-score" class="comment-score"></div><div class="comment-text"><p>Kurt,</p><p>As per your suggested I opened preferences file in Notepad, edited it and saved it without any error.</p><p>I tried to start it as an Administrator from Start Menu and Program Files\wireshark\wireshark.exe still facing the same issue.</p><p>Checked the Permission for Wireshark folder in C:\Users\Current user\AppData\Roaming\Wireshark, it does have full access.</p><p>Thanks, Prashant</p></div><div id="comment-32685-info" class="comment-info"><span class="comment-age">(09 May '14, 12:44)</span> <span class="comment-user userinfo">prashant4uall</span></div></div><span id="32693"></span><div id="comment-32693" class="comment"><div id="post-32693-score" class="comment-score"></div><div class="comment-text"><blockquote><p>tried to start it as an Administrator from Start Menu</p></blockquote><p>Did you also try to start it as user <strong>Admin</strong> (as shown in the path)?</p><blockquote><p>C:\Users\Current user\AppData\Roaming\Wireshark</p></blockquote><p>Did you also check the path</p><blockquote><p>C:\Users\<strong>Admin</strong>\Application Data\Wireshark</p></blockquote><p>or is that the same?</p></div><div id="comment-32693-info" class="comment-info"><span class="comment-age">(09 May '14, 15:19)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-32671" class="comment-tools"></div><div class="clear"></div><div id="comment-32671-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

