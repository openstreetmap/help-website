+++
type = "question"
title = "error compiling wireshark after successful configuration"
description = '''Trying to compile wireshark, I had several errors in the environment setup/configuration step that I worked through.  Now I am following the user guide at https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html. I am at the &quot;msbuild /m /p:Configuration=RelWithDebInfo Wireshark.sln&quot; step 2...'''
date = "2017-04-10T08:41:00Z"
lastmod = "2017-04-11T01:43:00Z"
weight = 60707
keywords = [ "dissector", "build", "wireshark-2.2.5" ]
aliases = [ "/questions/60707" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [error compiling wireshark after successful configuration](/questions/60707/error-compiling-wireshark-after-successful-configuration)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60707-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60707-score" class="post-score" title="current number of votes">0</div><span id="post-60707-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Trying to compile wireshark, I had several errors in the environment setup/configuration step that I worked through.<br />
</p><p>Now I am following the user guide at <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html.">https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html.</a> I am at the "msbuild /m /p:Configuration=RelWithDebInfo Wireshark.sln" step 2.2.12. The first error I see is</p><pre><code>94&gt;CustomBuild:
     Generating developer-guide.xml
     &#39;LC_ALL&#39; is not recognized as an internal or external command,
     operable program or batch file.
94&gt;C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppComm
   on.targets(170,5): error MSB6006: &quot;cmd.exe&quot; exited with code 9009. [C:\w
   ireshark_development\development\wsbuild64\docbook\generate_developer-gu
   ide.xml.vcxproj]</code></pre><p>So, I looked up to see if other users had this problem, and they were told to ensure Cywin packages for AsciiDoc and DocbookXML were installed. But the funny thing is, the Cygwin package I was told to install as part of the setup doesn't have the option for those 2 packages. So I'm left wondering if I have some weird mismatch between tool and wireshark source versions and installation instructions.</p><p>Incidentally, I am compiling this in order to compile a dissector. I can post other captures as need be.</p><p>Thanks, Brett</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span> <span class="post-tag tag-link-wireshark-2.2.5" rel="tag" title="see questions tagged &#39;wireshark-2.2.5&#39;">wireshark-2.2.5</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Apr '17, 08:41</strong></p><img src="https://secure.gravatar.com/avatar/633e258fc32dcd96044c6412f161fcf7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="szuderac&#39;s gravatar image" /><p><span>szuderac</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="szuderac has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Apr '17, 09:03</strong> </span></p></div></div><div id="comments-container-60707" class="comments-container"></div><div id="comment-tools-60707" class="comment-tools"></div><div class="clear"></div><div id="comment-60707-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60708"></span>

<div id="answer-container-60708" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60708-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60708-score" class="post-score" title="current number of votes">0</div><span id="post-60708-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="szuderac has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You'll have to run Cygwin setup to install asciidoc and docbook-xml45 as per the instructions.</p><p>You can also use chocolatey (although I have had issues with this):</p><pre><code>choco inst -y asciidoc docbook-xml45 -source Cygwin</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Apr '17, 10:12</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-60708" class="comments-container"><span id="60710"></span><div id="comment-60710" class="comment"><div id="post-60710-score" class="comment-score"></div><div class="comment-text"><p>For whatever reason, when I was installing cygwin direct from the setup guide before it didn't even have the option for those 2 components under text, it only had 3 elements. Now I'm trying it again and they are there, so I am attempting it again after that install goes through. Thanks.</p></div><div id="comment-60710-info" class="comment-info"><span class="comment-age">(10 Apr '17, 11:23)</span> <span class="comment-user userinfo">szuderac</span></div></div><span id="60726"></span><div id="comment-60726" class="comment"><div id="post-60726-score" class="comment-score"></div><div class="comment-text"><p><span>@szuderac</span></p><p>Your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-60726-info" class="comment-info"><span class="comment-age">(11 Apr '17, 01:43)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-60708" class="comment-tools"></div><div class="clear"></div><div id="comment-60708-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

