+++
type = "question"
title = "Modify script to output multiple files"
description = '''Im new to scripting and tshark but managed to make this small script using examples from this page. It works very well but I&#x27;d like to modify it so it creates a new .txt file for every input file instead of writing it all to the same file. If someone could help me it would be much appreciated! @echo...'''
date = "2017-02-10T02:20:00Z"
lastmod = "2017-02-10T05:39:00Z"
weight = 59321
keywords = [ "tshark", "script" ]
aliases = [ "/questions/59321" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Modify script to output multiple files](/questions/59321/modify-script-to-output-multiple-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59321-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Im new to scripting and tshark but managed to make this small script using examples from this page. It works very well but I'd like to modify it so it creates a new .txt file for every input file instead of writing it all to the same file. If someone could help me it would be much appreciated!</p><pre><code>@echo off

set cap_files=&quot;*&quot;
set cap_folder=&quot;c:\test\&quot;

set outfile=C:\Users\Administrator\Desktop\New\outfile.txt

set tshark_cmd=&quot;C:\Program Files\Wireshark\tshark&quot;
set tshark_options= -q -z conv,tcp -z conv,udp

echo. &gt; %outfile%

for /r %cap_folder% %%f in (%cap_files%) do (
echo Processing File: %%f

REM echo == File: %%f &gt;&gt; %outfile%
%tshark_cmd% -r %%f %tshark_options% &gt;&gt;%outfile%
)

echo.
echo Results in: %outfile%</code></pre></div><div id="question-tags" class="tags-container tags">tshark script</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '17, 02:20</strong></p><img src="https://secure.gravatar.com/avatar/2b55b040ef13c2d0b86bd0711b2a9b4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="laminatorius&#39;s gravatar image" /><p>laminatorius<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="laminatorius has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Feb '17, 05:34</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-59321" class="comments-container"></div><div id="comment-tools-59321" class="comment-tools"></div><div class="clear"></div><div id="comment-59321-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59324"></span>

<div id="answer-container-59324" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59324-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you look in the dos help for for, e.g. <code>help for</code>, you can see there are extended subsititions of the "for" variable:</p><pre><code>In addition, substitution of FOR variable references has been enhanced.
You can now use the following optional syntax:

    %~I         - expands %I removing any surrounding quotes (&quot;)
    %~fI        - expands %I to a fully qualified path name
    %~dI        - expands %I to a drive letter only
    %~pI        - expands %I to a path only
    %~nI        - expands %I to a file name only
    %~xI        - expands %I to a file extension only
    %~sI        - expanded path contains short names only
    %~aI        - expands %I to file attributes of file
    %~tI        - expands %I to date/time of file
    %~zI        - expands %I to size of file
    %~$PATH:I   - searches the directories listed in the PATH
                   environment variable and expands %I to the
                   fully qualified name of the first one found.
                   If the environment variable name is not
                   defined or the file is not found by the
                   search, then this modifier expands to the
                   empty string

The modifiers can be combined to get compound results:

    %~dpI       - expands %I to a drive letter and path only
    %~nxI       - expands %I to a file name and extension only</code></pre><p>So, using <code>%%~dpnf.txt</code> will get you the input filename, but with a .txt extension.</p><p>You should also change the output redirection operator to be <code>&gt;</code> to overwrite each target text file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '17, 05:39</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-59324" class="comments-container"><span id="59327"></span><div id="comment-59327" class="comment"><div id="post-59327-score" class="comment-score"></div><div class="comment-text"><p>Thank you! That worked very well and was much easier than I thought.</p><hr /><p>You should also change the output redirection operator to be &gt; to overwrite each target text file.</p><hr /><p>I don't understand that part though. What exactly is the "output redirection operator" and why would it be better to overwrite the target text file? The Text files are generated with this script, there is nothing to overwrite. Or am I missing the point?</p></div><div id="comment-59327-info" class="comment-info"><span class="comment-age">(10 Feb '17, 07:13)</span> laminatorius</div></div><span id="59328"></span><div id="comment-59328" class="comment"><div id="post-59328-score" class="comment-score"></div><div class="comment-text"><p>The <code>&gt;&gt;</code> operator appends output to any pre-existing content. The <code>&gt;</code> operator overwrites any pre-existing content.</p><p>Using the append operator could trip you up if re-running the batch file over the same captures with different tshark options.</p><p>See <a href="https://ss64.com/nt/syntax-redirection.html">here</a> for info about redirection.</p></div><div id="comment-59328-info" class="comment-info"><span class="comment-age">(10 Feb '17, 07:35)</span> grahamb ♦</div></div><span id="59329"></span><div id="comment-59329" class="comment"><div id="post-59329-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-59329-info" class="comment-info"><span class="comment-age">(10 Feb '17, 07:35)</span> grahamb ♦</div></div></div><div id="comment-tools-59324" class="comment-tools"></div><div class="clear"></div><div id="comment-59324-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

