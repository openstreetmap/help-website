+++
type = "question"
title = "Where can I find a list of file formats by extension?"
description = '''I&#x27;ve come across various lists of file formats that Wireshark can open, but is there a list of the associated file extensions anywhere? (E.g. .cap, .pcap, .pcapng, .dmp, etc.)'''
date = "2013-10-30T07:33:00Z"
lastmod = "2013-11-04T08:01:00Z"
weight = 26539
keywords = [ "file-format", "wireshark" ]
aliases = [ "/questions/26539" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Where can I find a list of file formats by extension?](/questions/26539/where-can-i-find-a-list-of-file-formats-by-extension)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26539-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've come across various lists of <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChIOOpenSection.html#ChIOInputFormatsSection">file formats</a> that Wireshark can open, but is there a list of the associated file extensions anywhere? (E.g. <em>.cap,</em> .pcap, <em>.pcapng,</em> .dmp, etc.)</p></div><div id="question-tags" class="tags-container tags">file-format wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Oct '13, 07:33</strong></p><img src="https://secure.gravatar.com/avatar/310c7b54264c9e10ad43acb3bb1d042a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wiggers&#39;s gravatar image" /><p>wiggers<br />
<span class="score" title="31 reputation points">31</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wiggers has no accepted answers">0%</span></p></div></div><div id="comments-container-26539" class="comments-container"></div><div id="comment-tools-26539" class="comment-tools"></div><div class="clear"></div><div id="comment-26539-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="26542"></span>

<div id="answer-container-26542" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26542-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark does <em>not</em> use file extensions to determine the type of a capture file. The extension, if any, of a capture file can actually be anything; Wireshark tries to determine the type of the file by reading the file and looking for "magic" constants and using various heuristics,</p><p>Wireshark does have a list file extensions used only (AFAIK) to display a list of suggested extensions in the GUI when opening/saving a file.</p><p>(Note: previous list removed since it was incomplete)</p><p>One way to see a list is to do (with Windows Wireshark) a "File ! Open" and click on the "File Types" drop-down.</p><p>To repeat, the real take-away is that capture file extensions are only, in some cases, a hint as to the type of the capture file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Oct '13, 08:07</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Oct '13, 08:44</p></div></div><div id="comments-container-26542" class="comments-container"><span id="26544"></span><div id="comment-26544" class="comment"><div id="post-26544-score" class="comment-score"></div><div class="comment-text"><p>"Wireshark does not use file extensions to determine the type of a capture file." That wasn't my question! Thanks for the list, that is what I was after.</p><p>Edit: D'oh! Good thing I copied it before you deleted it. No, the take away is not that Wireshark is very clever at sorting out file formats. I need to know the file extensions for another tool that calls tshark. It has to handle over 70 different file formats besides capture files.</p></div><div id="comment-26544-info" class="comment-info"><span class="comment-age">(30 Oct '13, 08:15)</span> wiggers</div></div><span id="26549"></span><div id="comment-26549" class="comment"><div id="post-26549-score" class="comment-score"></div><div class="comment-text"><p>Ok, but I assume you've picked up that the file extension can be a poor indicator of the file format itself. So even if the extension matches one of the many shown in the list below, it's no guarantee that it will be understood by tshark.</p></div><div id="comment-26549-info" class="comment-info"><span class="comment-age">(30 Oct '13, 10:27)</span> Jaap ♦</div></div></div><div id="comment-tools-26542" class="comment-tools"></div><div class="clear"></div><div id="comment-26542-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26543"></span>

<div id="answer-container-26543" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26543-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It doesn't really matter what the extension is, Wireshark will let you know if it can't handle the file. AFAICT the only uses for the extension are; a human readable reminder, and so that certain OS's can instantiate the correct executable when given the file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Oct '13, 08:10</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-26543" class="comments-container"><span id="26545"></span><div id="comment-26545" class="comment"><div id="post-26545-score" class="comment-score"></div><div class="comment-text"><p>Doesn't answer the question.</p></div><div id="comment-26545-info" class="comment-info"><span class="comment-age">(30 Oct '13, 08:15)</span> wiggers</div></div><span id="26548"></span><div id="comment-26548" class="comment"><div id="post-26548-score" class="comment-score">1</div><div class="comment-text"><p>The Windows installer does register a list of file extensions that it will claim if no other application is already registered for them. See <a href="http://anonsvn.wireshark.org/wireshark/trunk/packaging/nsis/common.nsh">http://anonsvn.wireshark.org/wireshark/trunk/packaging/nsis/common.nsh</a></p><p>The current list is given here: !macro PushFileExtensions Push "${FILE_EXTENSION_MARKER}" Push ".wpz" Push ".wpc" Push ".vwr" Push ".trc" Push ".trace" Push ".tr1" Push ".tpc" Push ".syc" Push ".snoop" Push ".rf5" Push ".pkt" Push ".pcapng" Push ".pcap" Push ".out" Push ".ntar" Push ".fdc" Push ".erf" Push ".enc" Push ".cap" Push ".bfr" Push ".atc" Push ".apc" Push ".acp" Push ".5vw" !macroend</p><p>As Graham said, the file extensions is no guarantee that Wireshark will be able to load the file, and other files without those extensions may well be usable.</p></div><div id="comment-26548-info" class="comment-info"><span class="comment-age">(30 Oct '13, 09:00)</span> MartinM</div></div></div><div id="comment-tools-26543" class="comment-tools"></div><div class="clear"></div><div id="comment-26543-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26547"></span>

<div id="answer-container-26547" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26547-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Here are screencaps from the Windows version: <img src="https://osqa-ask.wireshark.org/upfiles/wireshark_extns.png" alt="alt text" /> <img src="https://osqa-ask.wireshark.org/upfiles/wireshark_extns2.png" alt="alt text" /> <img src="https://osqa-ask.wireshark.org/upfiles/wireshark_extns3.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Oct '13, 08:59</strong></p><img src="https://secure.gravatar.com/avatar/310c7b54264c9e10ad43acb3bb1d042a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wiggers&#39;s gravatar image" /><p>wiggers<br />
<span class="score" title="31 reputation points">31</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wiggers has no accepted answers">0%</span></p></img></div></div><div id="comments-container-26547" class="comments-container"></div><div id="comment-tools-26547" class="comment-tools"></div><div class="clear"></div><div id="comment-26547-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26663"></span>

<div id="answer-container-26663" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26663-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I need to know the file extensions for <strong>another tool that calls tshark</strong>. It has to handle over 70 different file formats besides capture files.</p></blockquote><p>In that case it's better to use <strong><code>capinfos -t</code></strong> to figure out if it is a supported capture file type, <strong>regardless of the file extension!</strong></p><blockquote><p>capinfos -t dualhome.iptrace</p></blockquote><pre><code>File name:           dualhome.iptrace
File type:           AIX iptrace 2.0</code></pre><blockquote><p>capinfos -t k1.pcap</p></blockquote><pre><code>File name:           k1.pcap
File type:           Wireshark/... - pcapng</code></pre><blockquote><p>capinfos -t k1.txt</p></blockquote><pre><code>capinfos: Can&#39;t open k1.txt: The file isn&#39;t a capture file in a known format</code></pre><p>As you can see, if capinfos does not know the capture file type, it will print an error message and you can skip the file in your tool, as tshark won't understand it either. capinfos and tshark use the same mechanism to detect the capture file type, <strong>regardless of the file extension!</strong>.</p><p>Besides the error message, you can also use the exit code of capinfos (%errorlevel% on windows and $? on UN*Xes).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Nov '13, 08:01</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 04 Nov '13, 13:27</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></img></div></div><div id="comments-container-26663" class="comments-container"></div><div id="comment-tools-26663" class="comment-tools"></div><div class="clear"></div><div id="comment-26663-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

