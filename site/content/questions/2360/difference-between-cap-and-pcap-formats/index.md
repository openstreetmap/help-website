+++
type = "question"
title = "difference between cap and pcap formats??"
description = '''what is the difference between .cap and .pcap formats?? Thanks and Regards, Sid'''
date = "2011-02-16T00:19:00Z"
lastmod = "2011-02-16T11:23:00Z"
weight = 2360
keywords = [ "wireshark" ]
aliases = [ "/questions/2360" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [difference between cap and pcap formats??](/questions/2360/difference-between-cap-and-pcap-formats)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2360-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>what is the difference between .cap and .pcap formats??</p><p>Thanks and Regards,</p><p>Sid</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '11, 00:19</strong></p><img src="https://secure.gravatar.com/avatar/5a41ae1c710064aebdb9a4e0a1788d12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sid&#39;s gravatar image" /><p>sid<br />
<span class="score" title="45 reputation points">45</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sid has no accepted answers">0%</span></p></div></div><div id="comments-container-2360" class="comments-container"></div><div id="comment-tools-2360" class="comment-tools"></div><div class="clear"></div><div id="comment-2360-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="2361"></span>

<div id="answer-container-2361" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2361-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>From my point of view ".cap" is the Network General Sniffer format while ".pcap" is the TCPDump/Wireshark format, although I guess that a lot of analyzers name their format ".cap". Main difference is in the headers of the file and frames, meaning that they contain different amounts of information about frames. They all have at least sizing and timing informations as well as the content of the captured frame (as much bytes as the frame slicing setting allowed).</p><p>The Network General .cap Format has additional info about channel numbers for example which the standard pcap format doesn't as far as I know (as long as you don't have optional PPI information headers).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '11, 01:06</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-2361" class="comments-container"><span id="2408"></span><div id="comment-2408" class="comment"><div id="post-2408-score" class="comment-score"></div><div class="comment-text"><p>Yes, analyzers other than the (Windows) Sniffer such as Microsoft Network Monitor, use .cap as the file suffix.</p><p>Wi-Fi channel number information <em>is</em> available in pcap and pcap-ng files, with the PPI link-layer type as well as with the radiotap, AVS, and Prism link-layer types. (The radio information is part of the "raw" packet data, not part of the file format itself, in pcap and pcap-ng formats; that's true of all those formats, including PPI.)</p></div><div id="comment-2408-info" class="comment-info"><span class="comment-age">(17 Feb '11, 21:46)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-2361" class="comment-tools"></div><div class="clear"></div><div id="comment-2361-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2362"></span>

<div id="answer-container-2362" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2362-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is an all too common misconception amongst MS OS users, that the file name extension <em>defines</em> the file format. In reality it only <em>hints</em> to it, for the sake of human users. In reality the file format has to be defined <em>by external means</em>, like a MIME type or a magic number in the file header.</p><p>Coming back to the original question: What is the difference between the file formats of files with the extension .cap vs. .pcap, that question is hard to answer definitively, as Jasper already mentioned. .cap could hint the a Network General Sniffer format file, but in reality, going with the defacto 3 character file extension on MS OS's, the libpcap format is most likely. The .pcap extension definitely hints in that direction.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '11, 01:50</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-2362" class="comments-container"><span id="2364"></span><div id="comment-2364" class="comment"><div id="post-2364-score" class="comment-score"></div><div class="comment-text"><p>Thats why I said "from my point of view", which is based on what kind of files I usually work with. I didn't say nor expect the extension to define the format - I know that the extension doesn't have anything to do with the actual file format :-)</p><p>In fact I had a lot of "fun" with capture file format, especially the totally chaotic pcap format with magic numbers that are the same for different structures...</p></div><div id="comment-2364-info" class="comment-info"><span class="comment-age">(16 Feb '11, 02:08)</span> Jasper ♦♦</div></div><span id="2409"></span><div id="comment-2409" class="comment"><div id="post-2409-score" class="comment-score"></div><div class="comment-text"><p>If by "magic numbers" you mean the magic number at the beginning of the file, the only difference between the structures for standard pcap format is the byte order of the values, and that's the difference in the magic number as well - the intent was to have the program writing the file be able to write the file in its native byte order, rather than having to swap bytes while capturing, and have the program <em>reading</em> the file, which probably isn't as time-critical (no worry about dropping packets) do the byte-swapping when reading.</p></div><div id="comment-2409-info" class="comment-info"><span class="comment-age">(17 Feb '11, 21:48)</span> Guy Harris ♦♦</div></div><span id="2429"></span><div id="comment-2429" class="comment"><div id="post-2429-score" class="comment-score"></div><div class="comment-text"><p>I just remember reading some tap code in the Wireshark source where two pcap file "formats" are using the same magic number and then there is a catch block to see if an exception is raised. If it does, it's the one format, if not, it's the other. That kind of thing :-)</p></div><div id="comment-2429-info" class="comment-info"><span class="comment-age">(19 Feb '11, 11:22)</span> Jasper ♦♦</div></div><span id="2430"></span><div id="comment-2430" class="comment"><div id="post-2430-score" class="comment-score"></div><div class="comment-text"><p>OK, that's actually the fault of some people <em>misusing</em> the pcap format, by changing it but not also changing the magic number. If the pcap format is used correctly, that's not necessary (and libpcap doesn't bother with that workaround, mainly because it has to support reading from a pipe, and that sort of crap is harder in that case).</p></div><div id="comment-2430-info" class="comment-info"><span class="comment-age">(19 Feb '11, 11:25)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-2362" class="comment-tools"></div><div class="clear"></div><div id="comment-2362-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2385"></span>

<div id="answer-container-2385" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2385-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Uh... my first inclination is to answer "a letter."</p><p>Note that when analyzing .pcap or .cap files, Wireshark displays the same information.</p><p>Maybe we need to know why you asked the question... just curious or is there a need to understand if there are potential differences in file contents and support...</p><p>Lordy I couldn't reference Network General stuff anymore... been too many years since I played with those Sniffers... (or the old LANalyzer... sniff, sniff...). He he.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '11, 11:23</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p>lchappell ♦<br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-2385" class="comments-container"></div><div id="comment-tools-2385" class="comment-tools"></div><div class="clear"></div><div id="comment-2385-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

