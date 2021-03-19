+++
type = "question"
title = "Wireshak capture drive."
description = '''Hello, My drive c is full and when I am running the wireshark I get the error message low disk space. how can I change the drive where the packets are being captured. I do not mean when I save the capture but when the capture is being run I would like the packets to be stored in drive D. BR, V. Nico...'''
date = "2011-03-01T05:47:00Z"
lastmod = "2011-03-01T06:15:00Z"
weight = 2604
keywords = [ "shortkey" ]
aliases = [ "/questions/2604" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshak capture drive.](/questions/2604/wireshak-capture-drive)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2604-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>My drive c is full and when I am running the wireshark I get the error message low disk space. how can I change the drive where the packets are being captured. I do not mean when I save the capture but when the capture is being run I would like the packets to be stored in drive D.</p><p>BR, V. Nicolau</p></div><div id="question-tags" class="tags-container tags">shortkey</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Mar '11, 05:47</strong></p><img src="https://secure.gravatar.com/avatar/4fea27093ec00a668978eed6bdd2a9ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="VictorNicolau&#39;s gravatar image" /><p>VictorNicolau<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="VictorNicolau has no accepted answers">0%</span></p></div></div><div id="comments-container-2604" class="comments-container"></div><div id="comment-tools-2604" class="comment-tools"></div><div class="clear"></div><div id="comment-2604-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2606"></span>

<div id="answer-container-2606" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2606-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark (on windows) will use the environment variable <code>%TEMP%</code> to determine where to store the temporary files while capturing. If that fails it falls back to <code>C:\</code></p><p>So make sure <code>%TEMP%</code> points to a directory on drive D.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '11, 06:15</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-2606" class="comments-container"><span id="2608"></span><div id="comment-2608" class="comment"><div id="post-2608-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer unfortunately for me this solution will not work because the machine I am using wireshark on as to have the Temp directed to drive c otherwise the specific application does not work.</p></div><div id="comment-2608-info" class="comment-info"><span class="comment-age">(01 Mar '11, 07:07)</span> VictorNicolau</div></div><span id="2611"></span><div id="comment-2611" class="comment"><div id="post-2611-score" class="comment-score">1</div><div class="comment-text"><p>If you can't change the system temp directory you could set a temporary temp path for just one run of Wireshark. To do that, open a command prompt and type</p><p><code>set temp=d:\temp</code> (press enter. )</p><p>Then, in the same command prompt, start Wireshark (usually by running <code>c:\program files\wireshark\wireshark.exe</code>, though it may be different on your machine). I have the Wireshark directory in my system path, so I could just call wireshark.exe.</p><p>You can automate this by writing a small batch file that sets the temp path before calling wireshark.exe, then create a shortcut and assign the Wireshark.exe icon to it.</p></div><div id="comment-2611-info" class="comment-info"><span class="comment-age">(01 Mar '11, 08:59)</span> Jasper ♦♦</div></div><span id="2620"></span><div id="comment-2620" class="comment"><div id="post-2620-score" class="comment-score"></div><div class="comment-text"><p>(converted the "answers" to "comments" to adhere to the Q&amp;A character of this site)</p></div><div id="comment-2620-info" class="comment-info"><span class="comment-age">(01 Mar '11, 14:09)</span> SYN-bit ♦♦</div></div><span id="2628"></span><div id="comment-2628" class="comment"><div id="post-2628-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot. This is a good solution for me. Now I just need to know how to write a Batch file and associate the wireshark .exe icon to it.</p><p>BR, V. Nicolau</p></div><div id="comment-2628-info" class="comment-info"><span class="comment-age">(02 Mar '11, 05:24)</span> VictorNicolau</div></div><span id="2668"></span><div id="comment-2668" class="comment"><div id="post-2668-score" class="comment-score"></div><div class="comment-text"><p>A batch file is just a text file that you can create with any text editor. In that file you write all commands, usually one per line, and save the complete file with a ".cmd" or ".bat" extension. That way you can execute it as a batch.</p><p>To assign an icon you might want to create a shortcut of the batch file and then use the shortcut properties to change the icon. Browse to the wireshark executable and select it as icon source.</p></div><div id="comment-2668-info" class="comment-info"><span class="comment-age">(04 Mar '11, 12:38)</span> Jasper ♦♦</div></div></div><div id="comment-tools-2606" class="comment-tools"></div><div class="clear"></div><div id="comment-2606-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

