+++
type = "question"
title = "UTC time with -T fields"
description = '''Am I missing something or is there really no UTC option for the -T fields call?  I know you can get UTC time normally with &quot;tshark -r C:&#92;infile.pcap&quot; but I need more specific headers than what the summary info can provide and -e frame.time is only passing local time. I am analyzing pcap files from a...'''
date = "2014-03-15T10:18:00Z"
lastmod = "2016-07-11T02:58:00Z"
weight = 30818
keywords = [ "utc", "time", "tshark", "timestamp", "fields" ]
aliases = [ "/questions/30818" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [UTC time with -T fields](/questions/30818/utc-time-with-t-fields)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30818-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Am I missing something or is there really no UTC option for the <code>-T fields</code> call?</p><p>I know you can get UTC time normally with "<code>tshark -r C:\infile.pcap</code>" but I need more specific headers than what the summary info can provide and <code>-e frame.time</code> is only passing local time. I am analyzing pcap files from all over the country, so I can't set a standard rule like <code>frame.time +- TZ</code>. The only thing I can think of doing is doing 2 separate calls:</p><pre><code>tshark -r C:\infile.pcap -c 1

tshark -r C:\infile.pcap -T fields -e frame.time_relative -e blah blah</code></pre><p>and then programmatically adding the relative time to the first packet time gained in the first <code>tshark</code> call.</p><p>But there has to be a better solution then this, right? <code>tshark</code> wouldn't leave UTC time out when you can set a field for it in <strong>Wireshark</strong> and you can get it without calling <code>-T fields</code>?</p><p>Thanks guys,</p><p>Update -</p><p>Does anyone know if you need wireshark or anything releated to wireshark (other than tshark) to use the call:</p><p>tshark.exe -r C:\Users\zmcpher\Desktop\1.pcap -o "gui.column.format:\"UTC Time\",\"%Aut\"</p><p>This seems to do what I need - so Im hoping it will works with only tshark libraries.</p></div><div id="question-tags" class="tags-container tags">utc time tshark timestamp fields</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Mar '14, 10:18</strong></p><img src="https://secure.gravatar.com/avatar/fbc5b3a06e0bdd9408c2356da21566c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nefarii&#39;s gravatar image" /><p>Nefarii<br />
<span class="score" title="31 reputation points">31</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nefarii has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Mar '14, 11:53</p></div></div><div id="comments-container-30818" class="comments-container"><span id="30833"></span><div id="comment-30833" class="comment"><div id="post-30833-score" class="comment-score"></div><div class="comment-text"><p>It doesn't look like it depends on the GUI code at all - just the preferences code; but you should try it on a target system.</p></div><div id="comment-30833-info" class="comment-info"><span class="comment-age">(15 Mar '14, 12:40)</span> Hadriel</div></div></div><div id="comment-tools-30818" class="comment-tools"></div><div class="clear"></div><div id="comment-30818-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="30822"></span>

<div id="answer-container-30822" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30822-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You mean like one of these?:</p><pre><code>tshark -t u
tshark -t ud</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '14, 11:29</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-30822" class="comments-container"><span id="30823"></span><div id="comment-30823" class="comment"><div id="post-30823-score" class="comment-score"></div><div class="comment-text"><p>Oops... answer collisions. :)</p></div><div id="comment-30823-info" class="comment-info"><span class="comment-age">(15 Mar '14, 11:30)</span> Hadriel</div></div><span id="30825"></span><div id="comment-30825" class="comment"><div id="post-30825-score" class="comment-score"></div><div class="comment-text"><p>Ive tried -t, but I cant seem to use it in conjunction with -T</p></div><div id="comment-30825-info" class="comment-info"><span class="comment-age">(15 Mar '14, 11:41)</span> Nefarii</div></div><span id="30826"></span><div id="comment-30826" class="comment"><div id="post-30826-score" class="comment-score"></div><div class="comment-text"><p>In what way? What fields are you trying to extract?</p></div><div id="comment-30826-info" class="comment-info"><span class="comment-age">(15 Mar '14, 11:46)</span> Hadriel</div></div><span id="30845"></span><div id="comment-30845" class="comment"><div id="post-30845-score" class="comment-score"></div><div class="comment-text"><p>Hmm, it seems that the <a href="http://www.wireshark.org/docs/man-pages/tshark.html">online tshark man page</a> is missing the <code>-t u</code> and <code>-t ud</code> options.</p></div><div id="comment-30845-info" class="comment-info"><span class="comment-age">(15 Mar '14, 14:01)</span> cmaynard ♦♦</div></div><span id="30846"></span><div id="comment-30846" class="comment"><div id="post-30846-score" class="comment-score"></div><div class="comment-text"><p>Should have been... unless it was missed somehow by <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8906">bug 8906</a>?</p></div><div id="comment-30846-info" class="comment-info"><span class="comment-age">(15 Mar '14, 14:33)</span> Hadriel</div></div><span id="30847"></span><div id="comment-30847" class="comment not_top_scorer"><div id="post-30847-score" class="comment-score"></div><div class="comment-text"><p>Well it's definitely in the real man pages installed. I wonder where the online ones come from. (buildbots?)</p></div><div id="comment-30847-info" class="comment-info"><span class="comment-age">(15 Mar '14, 14:42)</span> Hadriel</div></div></div><div id="comment-tools-30822" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-30822-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53978"></span>

<div id="answer-container-53978" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53978-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>This might help:</p><pre><code>tshark -r C:\infile.pcap -T fields -e frame.time_epoch -e blah blah</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jul '16, 02:58</strong></p><img src="https://secure.gravatar.com/avatar/52d600a0425fd5e6a7306e84605b027d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arashdalir&#39;s gravatar image" /><p>arashdalir<br />
<span class="score" title="51 reputation points">51</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arashdalir has no accepted answers">0%</span></p></div></div><div id="comments-container-53978" class="comments-container"></div><div id="comment-tools-53978" class="comment-tools"></div><div class="clear"></div><div id="comment-53978-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30821"></span>

<div id="answer-container-30821" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30821-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could use something very similar to the answers I provided for these 2 questions:</p><ul><li><a href="http://ask.wireshark.org/questions/30393/tshark-how-to-output-date-in-iso-format">tshark - How to output date in ISO format?</a></li><li><a href="http://ask.wireshark.org/questions/30799/how-do-i-display-absolute-time-and-delta-at-the-same-time-with-tshark">How do I display absolute time and delta at the same time with tshark?</a></li></ul><p>In your case, add either <em>"UTC date and time"</em> or <em>"UTC time"</em> and name the column something like <code>UTCDateTime</code> or <code>UTCTime</code>, respectively, and then you can use:</p><pre><code>tshark -r C:\infile.pcap -T fields -e col.UTCDateTime -e blah blah</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '14, 11:25</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-30821" class="comments-container"><span id="30824"></span><div id="comment-30824" class="comment"><div id="post-30824-score" class="comment-score"></div><div class="comment-text"><p>Sorry, I should of mentioned this - I have tshark bundled with one of my scripts, so you have to assume that wireshark is not installed on any of the PC's that will be runnning the script. So the -e col wont work</p></div><div id="comment-30824-info" class="comment-info"><span class="comment-age">(15 Mar '14, 11:39)</span> Nefarii</div></div></div><div id="comment-tools-30821" class="comment-tools"></div><div class="clear"></div><div id="comment-30821-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

