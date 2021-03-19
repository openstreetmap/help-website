+++
type = "question"
title = "Bug ? when open Wireshark by clicking on a .pcap file"
description = '''Problem with Wireshark 2.2.0 (v2.2.0-0-g5368c50 from master-2.2) on Windows 7, 64-bits When started Wireshark by clicking on file I got an error message: The file &quot;xxx.pcap&quot; doesn&#x27;t exist Then I was transferred to the File open menu.  From that menu the file was opened correctly.'''
date = "2016-09-21T04:41:00Z"
lastmod = "2016-09-21T13:44:00Z"
weight = 55708
keywords = [ "open", "bug", "file" ]
aliases = [ "/questions/55708" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Bug ? when open Wireshark by clicking on a .pcap file](/questions/55708/bug-when-open-wireshark-by-clicking-on-a-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55708-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Problem with Wireshark 2.2.0 (v2.2.0-0-g5368c50 from master-2.2) on Windows 7, 64-bits</p><p>When started Wireshark by clicking on file I got an error message: The file "xxx.pcap" doesn't exist</p><p>Then I was transferred to the File open menu. From that menu the file was opened correctly.</p></div><div id="question-tags" class="tags-container tags">open bug file</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Sep '16, 04:41</strong></p><img src="https://secure.gravatar.com/avatar/e137caab2ff703492e7ca349ac3c07eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christer%20G&#39;s gravatar image" /><p>Christer G<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christer G has no accepted answers">0%</span></p></div></div><div id="comments-container-55708" class="comments-container"><span id="55709"></span><div id="comment-55709" class="comment"><div id="post-55709-score" class="comment-score"></div><div class="comment-text"><p>(I assume you mean you're clicking on a file in Windows explorer?)</p><p>It works fine for me.</p><p>By chance are there any non-ASCII characters in the file or path name? (If you're not sure then just cut-n-paste the full path name here.)</p></div><div id="comment-55709-info" class="comment-info"><span class="comment-age">(21 Sep '16, 06:17)</span> JeffMorriss ♦</div></div><span id="55710"></span><div id="comment-55710" class="comment"><div id="post-55710-score" class="comment-score"></div><div class="comment-text"><p>One of the file names is Melsec_691_MsgId_1.pcap Another is 20130321.pcap With another extension 20130930.pcapng</p></div><div id="comment-55710-info" class="comment-info"><span class="comment-age">(21 Sep '16, 06:28)</span> Christer G</div></div><span id="55711"></span><div id="comment-55711" class="comment"><div id="post-55711-score" class="comment-score"></div><div class="comment-text"><p>The "clicking" is, as you presumed, in Windows Explorer. The folders have an underscore in their name.</p></div><div id="comment-55711-info" class="comment-info"><span class="comment-age">(21 Sep '16, 06:32)</span> Christer G</div></div><span id="55712"></span><div id="comment-55712" class="comment"><div id="post-55712-score" class="comment-score"></div><div class="comment-text"><p>Your "answers" has been converted to comments as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-55712-info" class="comment-info"><span class="comment-age">(21 Sep '16, 06:39)</span> grahamb ♦</div></div><span id="55715"></span><div id="comment-55715" class="comment"><div id="post-55715-score" class="comment-score"></div><div class="comment-text"><p>And there's nothing in <strong>full path</strong> (probably including your user name) that's not ASCII? (Just checking...)</p></div><div id="comment-55715-info" class="comment-info"><span class="comment-age">(21 Sep '16, 07:48)</span> JeffMorriss ♦</div></div><span id="55717"></span><div id="comment-55717" class="comment not_top_scorer"><div id="post-55717-score" class="comment-score"></div><div class="comment-text"><p>Yes there were. Thanks for the help.</p></div><div id="comment-55717-info" class="comment-info"><span class="comment-age">(21 Sep '16, 09:28)</span> Christer G</div></div></div><div id="comment-tools-55708" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-55708-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="55727"></span>

<div id="answer-container-55727" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55727-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Can you try one of the 2.2.1 <a href="https://www.wireshark.org/download/automated/">automated builds</a>? There was a <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12900">regression in 2.2.0</a> which kept Wireshark from handling multibyte characters correctly on the command line (which includes files opened from Windows Explorer). It will be fixed in 2.2.1.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Sep '16, 13:44</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-55727" class="comments-container"><span id="55817"></span><div id="comment-55817" class="comment"><div id="post-55817-score" class="comment-score"></div><div class="comment-text"><p>I observed exactly the same symptoms. In the file path I had these non-ASCII characters: "á" and "í". A new build of 2.2.1 (<a href="https://www.wireshark.org/download/automated/win64/Wireshark-win64-2.2.1rc0-48-g85abe17.exe">Wireshark-win64-2.2.1rc0-48-g85abe17.exe</a>) as suggested by Gerald Combs resolved the problem.</p></div><div id="comment-55817-info" class="comment-info"><span class="comment-age">(25 Sep '16, 15:42)</span> pabouk</div></div></div><div id="comment-tools-55727" class="comment-tools"></div><div class="clear"></div><div id="comment-55727-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="55723"></span>

<div id="answer-container-55723" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55723-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>OK, based on the comments (thanks for the responses) it looks like there's a problem if the full path of the opened-from-the-OS-file-browser file includes non-ASCII characters. This could be lumped into <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=1827">bug 1827</a> but it's probably/hopefully simpler than that never-ending bug.</p><p>I'd suggest <a href="https://bugs.wireshark.org/">opening a separate bug report</a> for this particular case.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Sep '16, 10:48</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-55723" class="comments-container"></div><div id="comment-tools-55723" class="comment-tools"></div><div class="clear"></div><div id="comment-55723-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

