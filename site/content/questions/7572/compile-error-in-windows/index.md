+++
type = "question"
title = "Compile error in windows"
description = '''Hi There, I tried to compile wireshark on a machine for the first time. I got the below given error.How to resolve this? perl perlnoutf.pl make-authors-short.pl &amp;lt; ../AUTHORS &amp;gt; AUTHORS-SHORT perl perlnoutf.pl make-authors-format.pl &amp;lt; AUTHORS-SHORT &amp;gt; AUTHORS-SHORT -FORMAT copy /B wireshark...'''
date = "2011-11-22T21:53:00Z"
lastmod = "2013-05-25T14:50:00Z"
weight = 7572
keywords = [ "compile", "error" ]
aliases = [ "/questions/7572" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Compile error in windows](/questions/7572/compile-error-in-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7572-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7572-score" class="post-score" title="current number of votes">0</div><span id="post-7572-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi There,</p><p>I tried to compile wireshark on a machine for the first time. I got the below given error.How to resolve this?</p><pre><code>perl perlnoutf.pl make-authors-short.pl &lt; ../AUTHORS &gt; AUTHORS-SHORT
perl perlnoutf.pl make-authors-format.pl &lt; AUTHORS-SHORT &gt; AUTHORS-SHORT -FORMAT
copy /B wireshark.pod.template + AUTHORS-SHORT-FORMAT wireshark.pod wireshark.pod.template

AUTHORS-SHORT-FORMAT
        1 file(s) copied.
copy ..\docbook\ws.css .
        1 file(s) copied.
bash -o igncr pod2html --title=&quot;The Wireshark Network Analyzer 1.6.1&quot;  --css=ws.css --noindex wireshark.pod &gt; wireshark.html

Can&#39;t execute /usr/bin/pod2html.
NMAKE : fatal error U1077: &#39;bash&#39; : return code &#39;0x1d&#39;
Stop.

NMAKE : fatal error U1077: &#39;&quot;C:\Program Files (x86)\Microsoft Visual Studio 9.0\
VC\BIN\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.</code></pre><p>Please Help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-compile" rel="tag" title="see questions tagged &#39;compile&#39;">compile</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Nov '11, 21:53</strong></p><img src="https://secure.gravatar.com/avatar/968cc7ddfc48322ffbd1d7f5e3d37b85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Terrestrial%20shark&#39;s gravatar image" /><p><span>Terrestrial ...</span><br />
<span class="score" title="96 reputation points">96</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="28 badges"><span class="silver">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Terrestrial shark has 3 accepted answers">42%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Nov '11, 23:27</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-7572" class="comments-container"><span id="7573"></span><div id="comment-7573" class="comment"><div id="post-7573-score" class="comment-score"></div><div class="comment-text"><p>I read in the <a href="http://msdn.microsoft.com/en-us/library/dt309377.aspx">microsoft site</a> that when the given command or program called by NMAKE failed then it returns the above given exit code U1077. As they suggested I used /I along with <code>nmake -f Makefile.nmake all /I</code>. It ignored the error and worked well but may I know How does that error completely get resolved?</p></div><div id="comment-7573-info" class="comment-info"><span class="comment-age">(22 Nov '11, 22:10)</span> <span class="comment-user userinfo">Terrestrial ...</span></div></div></div><div id="comment-tools-7572" class="comment-tools"></div><div class="clear"></div><div id="comment-7572-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7574"></span>

<div id="answer-container-7574" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7574-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7574-score" class="post-score" title="current number of votes">0</div><span id="post-7574-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I converted your "answer" to a comment.</p><p>It looks like your environment is lacking something and is unable to execute the pod2html script as can be seen by the line <code>Can't execute /usr/bin/pod2html</code>.</p><p>Check that the script is in the place indicated. If it isn't then you'll need to add a package to your Cygwin install that contains the script, see the Cygwin <a href="http://cygwin.com/packages/">Packages</a> page to search for one containing the required item.</p><p>If you do have the file then something else is wrong an you should see if the script can be executed from a Cygwin prompt, and work from there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '11, 23:34</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-7574" class="comments-container"><span id="7626"></span><div id="comment-7626" class="comment"><div id="post-7626-score" class="comment-score"></div><div class="comment-text"><p>pod2html is present inside <code>/usr/bin</code> directory. pod2html is running properly wireshark.pod and wireshark.pod.template. But it dint write anything into wireshark.html. when I execute <code>bash -o igncr pod2html --title="The Wireshark Network Analyzer 1.6.1"  --css=ws.css --noindex wireshark.pod &gt; wireshark.html</code></p><p>from cygwin. It errors as "Cant execute /usr/bin/pod2html"</p><p>What would be the problem? Please Help.</p></div><div id="comment-7626-info" class="comment-info"><span class="comment-age">(25 Nov '11, 01:27)</span> <span class="comment-user userinfo">Terrestrial ...</span></div></div></div><div id="comment-tools-7574" class="comment-tools"></div><div class="clear"></div><div id="comment-7574-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21141"></span>

<div id="answer-container-21141" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21141-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21141-score" class="post-score" title="current number of votes">0</div><span id="post-21141-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Here is what I did to make it work: Edit the file config.nmake and insert the full path for pod2man and pod2html as follows POD2MAN=$(SH) /usr/bin/pod2man</p><p>POD2HTML=$(SH) /usr/bin/pod2html</p><p>It should generate the proper man and html files. I think the problem is that the path to pod2man and pod2html is not passed to bash when running under nmake. If you try to run bash manually from the command line, it generates a html file with the appropriate size.</p><p>If this is indeed a general problem, can someone submit this fix to the wireshark developers?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 May '13, 10:49</strong></p><img src="https://secure.gravatar.com/avatar/07dadb40f98ad085187fd4d7d892ec7b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="makeadiff&#39;s gravatar image" /><p><span>makeadiff</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="makeadiff has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 May '13, 10:50</strong> </span></p></div></div><div id="comments-container-21141" class="comments-container"><span id="21147"></span><div id="comment-21147" class="comment"><div id="post-21147-score" class="comment-score"></div><div class="comment-text"><p>The build system as-is works perfectly for me, I just tested on trunk, and as far as I know also works well for others which leads me to believe that there is something odd in your build environment.</p></div><div id="comment-21147-info" class="comment-info"><span class="comment-age">(15 May '13, 05:02)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="21475"></span><div id="comment-21475" class="comment"><div id="post-21475-score" class="comment-score"></div><div class="comment-text"><p>Thanks for confirming that its not a general problem, now I'm sure its my build env. bash pod2html .... gives me an error, but bash /usr/bin/pod2html .... compiles fine. Any thoughts on what I'm missing?</p></div><div id="comment-21475-info" class="comment-info"><span class="comment-age">(25 May '13, 13:13)</span> <span class="comment-user userinfo">makeadiff</span></div></div><span id="21477"></span><div id="comment-21477" class="comment"><div id="post-21477-score" class="comment-score"></div><div class="comment-text"><p>Looking at the error it says "can't execute", maybe a permission problem?</p><p>I think you may have to hack the makefile in the problem area to print out some diagnostic info.</p></div><div id="comment-21477-info" class="comment-info"><span class="comment-age">(25 May '13, 14:50)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-21141" class="comment-tools"></div><div class="clear"></div><div id="comment-21141-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

