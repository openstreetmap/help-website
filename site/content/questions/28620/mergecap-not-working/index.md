+++
type = "question"
title = "Mergecap not working"
description = '''Good Morning, I was trying to capture several pcap files into one. I placed/saved the files on the desktop. Now on the recommendation of the book i entered the book verbatim, but i could not get it to work.Would you mind telling me how it works.  What do you think could be the reason. 1) Do i have t...'''
date = "2014-01-07T03:41:00Z"
lastmod = "2014-01-07T03:52:00Z"
weight = 28620
keywords = [ "mergecap" ]
aliases = [ "/questions/28620" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Mergecap not working](/questions/28620/mergecap-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28620-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Good Morning,</p><p>I was trying to capture several pcap files into one. I placed/saved the files on the desktop. Now on the recommendation of the book i entered the book verbatim, but i could not get it to work.Would you mind telling me how it works.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/df.png" alt="alt text" /></p><p>What do you think could be the reason.</p><p>1) Do i have to save the files in a different directory. 2) Seperately install mergecap.</p><p>Thanks Bharat CP</p></div><div id="question-tags" class="tags-container tags">mergecap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jan '14, 03:41</strong></p><img src="https://secure.gravatar.com/avatar/e689f2131ff3f3113d0b2cee2f420ebf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BharatNT2IE&#39;s gravatar image" /><p>BharatNT2IE<br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BharatNT2IE has no accepted answers">0%</span></p></img></div></div><div id="comments-container-28620" class="comments-container"></div><div id="comment-tools-28620" class="comment-tools"></div><div class="clear"></div><div id="comment-28620-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28621"></span>

<div id="answer-container-28621" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28621-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>You don't mention which book you are using, but it should have a section for Windows users on making sure that the wireshark binaries (which includes mergecap) is on your path.</p><p>The command shell is telling you that it doesn't know anything about mergecap, you'll need to adjust the path to include the wireshark binary path. Try executing</p><p><code>set PATH=%PATH%;path\to\wireshark</code></p><p>in your command shell, replacing <code>path\to\wireshark</code> with the actual path to wireshark on your machine, likely to be either <code>C:\Program Files\Wireshark</code> or <code>C:\Program Files (x86)\Wireshark</code> but it does depend on what OS you have and the version of Wireshark and the installation choices you made.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jan '14, 03:52</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-28621" class="comments-container"><span id="28622"></span><div id="comment-28622" class="comment"><div id="post-28622-score" class="comment-score"></div><div class="comment-text"><p>Wireshark 101 essential, the official wireshark one, i just looked at the glossary and it indicated me to that syntax, it should have been Windows, because the terminal looked like windows, but i will try your suggestion.</p></div><div id="comment-28622-info" class="comment-info"><span class="comment-age">(07 Jan '14, 04:04)</span> BharatNT2IE</div></div><span id="28623"></span><div id="comment-28623" class="comment"><div id="post-28623-score" class="comment-score"></div><div class="comment-text"><p>Graham,</p><p>Thank you for you help. All i did was to place the file in the default c folder, where the wireshark was installed, thank you very much, I will also try to get the path file.</p><p>So i did it in Windows 8 this is the path if anyone need to merge files.</p><p>C:\Program Files\Wireshark&gt;mergecap -w Meg.pcap Mergexxx<em>.</em></p><p>keep these files in the folder above and run the command.</p><p>Thanks Bharat C P</p><p>It worked Voila!!!!!</p><p>P.S. You might want to run the CMD as administrator.</p></div><div id="comment-28623-info" class="comment-info"><span class="comment-age">(07 Jan '14, 04:35)</span> BharatNT2IE</div></div><span id="28626"></span><div id="comment-28626" class="comment"><div id="post-28626-score" class="comment-score">2</div><div class="comment-text"><p>Its not a good idea to put capture files (or any data files you work with) into the program installation path. You should add the program installation path to the search path as @grahamb said.</p></div><div id="comment-28626-info" class="comment-info"><span class="comment-age">(07 Jan '14, 05:09)</span> Jasper ♦♦</div></div><span id="28627"></span><div id="comment-28627" class="comment"><div id="post-28627-score" class="comment-score"></div><div class="comment-text"><p>Jasper,</p><p>Yes, i will try that out and definitely get back to the group, i think i owe Graham that much. But for my purpose now it is served, but i will let the group know, i was just a bit unclear on the syntax, i will definitely let you know.</p><p>Thanks Bharat C P</p></div><div id="comment-28627-info" class="comment-info"><span class="comment-age">(07 Jan '14, 05:11)</span> BharatNT2IE</div></div><span id="28633"></span><div id="comment-28633" class="comment"><div id="post-28633-score" class="comment-score"></div><div class="comment-text"><p>Graham,</p><p>Thank you that worked, i was not sure of the working of the commands of that instruction</p><p><strong>set PATH=%PATH%;path\to\wireshark</strong></p><p>I have never used this command before, mix up by me. I followed your instruction verbatim and i got the desired results.</p><p>Here here goes, i hope some one can benefit from this.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Step1_2.jpg" alt="alt text" /></p><p>Once again appreciate it.</p><p>Thanks Bharat C P</p><p><img src="https://osqa-ask.wireshark.org/upfiles/STE33_2.jpg" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/STEP_5_1.png" alt="alt text" /></p></div><div id="comment-28633-info" class="comment-info"><span class="comment-age">(07 Jan '14, 07:22)</span> BharatNT2IE</div></div><span id="28641"></span><div id="comment-28641" class="comment not_top_scorer"><div id="post-28641-score" class="comment-score"></div><div class="comment-text"><p>Graham,</p><p>I am not quite done yet. Sorry about that,the previous example that was shown, i was merging files in windows. But this set i was trying to merge files that i took of MAC OSX. the problem that i am encountering</p><p>mergecap: Can't open or create xx.pcap: Files from that network type can't be saved in that format</p><p>the same syntax.</p><p>Please try to guide me in the right train of tought i am thinking MAC OSX the files by default are in libpcap, files, i even tried to change the extenstion to libpcap, with the same undesired result. Anay one is open for suggestion.</p><p>BTW. I was able to merge in MAC the group of files. But i wanted to know in the event of merging in MAC and find. Please any suggestion are welcome.</p><p>Thanks Bharat C P</p></div><div id="comment-28641-info" class="comment-info"><span class="comment-age">(07 Jan '14, 08:55)</span> BharatNT2IE</div></div><span id="28643"></span><div id="comment-28643" class="comment not_top_scorer"><div id="post-28643-score" class="comment-score"></div><div class="comment-text"><p>Graham, I do not seem to be able to view any of our comments is it a know bug.</p><p>Thanks Bharat</p></div><div id="comment-28643-info" class="comment-info"><span class="comment-age">(07 Jan '14, 09:40)</span> BharatNT2IE</div></div></div><div id="comment-tools-28621" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-28621-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

