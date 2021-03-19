+++
type = "question"
title = "How to filter specific phone number(s) during capture?"
description = '''I am trying to setup a way to filter for specific phone phones during a wireshark capture. I am not sure what filter I should use. I tried the sip.To and sdp.phone filters with no success. Any ideas? Thanks!'''
date = "2011-04-28T07:00:00Z"
lastmod = "2011-05-04T19:23:00Z"
weight = 3785
keywords = [ "filter", "phone", "numbers" ]
aliases = [ "/questions/3785" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [How to filter specific phone number(s) during capture?](/questions/3785/how-to-filter-specific-phone-numbers-during-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3785-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to setup a way to filter for specific phone phones during a wireshark capture. I am not sure what filter I should use. I tried the sip.To and sdp.phone filters with no success. Any ideas? Thanks!</p></div><div id="question-tags" class="tags-container tags">filter phone numbers</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Apr '11, 07:00</strong></p><img src="https://secure.gravatar.com/avatar/b50edfed37a017cee87d22dd87d19ef5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Travis%20Young&#39;s gravatar image" /><p>Travis Young<br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Travis Young has no accepted answers">0%</span></p></div></div><div id="comments-container-3785" class="comments-container"></div><div id="comment-tools-3785" class="comment-tools"></div><div class="clear"></div><div id="comment-3785-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="3799"></span>

<div id="answer-container-3799" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3799-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Capture filters based on BPF and predates any VoIP protocols. And you can't use display filters when capturing. However, if you have a limited number of phone numbers, you can always use byte offset syntax to specify the phone number. Lookup the syntax for specifying byte offset. For example, tcp[0:2] &gt; 1024 will capture tcp packets whose source port is greater than 1024.<br />
</p><p>The 0:2 means start at the first byte of the tcp header, and look at two bytes worth.</p><p>Look at http://acs.lbl.gov/~jason/tcpdump_advanced_filters.txt for some more examples on using filters and masks.<br />
</p><p>Might turn into a PIA project, but it can be done.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '11, 16:56</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p>hansangb<br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span> </br></br></p></div></div><div id="comments-container-3799" class="comments-container"><span id="3805"></span><div id="comment-3805" class="comment"><div id="post-3805-score" class="comment-score"></div><div class="comment-text"><p>The main reasons for BPF to be not as extensive as diplay filtering are:</p><ul><li>It needs to be as lean as possible to not overload the CPU</li><li>It needs to be lean as it is a kernal module</li><li>It can't branch backwords in the BPF code, so loops are prevented</li></ul></div><div id="comment-3805-info" class="comment-info"><span class="comment-age">(28 Apr '11, 23:00)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-3799" class="comment-tools"></div><div class="clear"></div><div id="comment-3799-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3800"></span>

<div id="answer-container-3800" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3800-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Since you mention <code>sip.To</code> and <code>sdp.phone</code>, I assume:</p><ol><li>you're looking for a <a href="http://wiki.wireshark.org/DisplayFilters">display filter</a> (and not a <a href="http://wiki.wireshark.org/CaptureFilters">capture filter</a>)</li><li>the only fields of interest (i.e., the ones you expect to contain phone numbers) are the ones mentioned; and thus, we're dealing with only SIP</li></ol><p>I don't claim to know SIP, but based on <a href="http://www.ietf.org/rfc/rfc3261.txt">RFC2361</a>, the <em>To Header Field</em> and <em>From Header Field</em> (both of which are string fields, terminated by <code>\r\n</code>) can contain phone numbers that look like these examples:</p><ul><li><code>tel:411</code></li><li><code>sip:[email protected];tag=887s</code></li></ul><p>So, let's say the target phone number is 555-123-4567. Your display filters would be:</p><ul><li>show SIP packets <em>to/from</em> this number: <strong><code>sip contains 5551234567</code></strong></li><li>show SIP packets <em>to</em> this number: <strong><code>sip.To contains 5551234567</code></strong></li><li>show SIP packets <em>from</em> this number: <strong><code>sip.From contains 5551234567</code></strong></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '11, 17:01</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-3800" class="comments-container"><span id="3817"></span><div id="comment-3817" class="comment"><div id="post-3817-score" class="comment-score">1</div><div class="comment-text"><p>Thanks for the advice thus far!</p><p>I would like to find a way to create a capture filter that can look for certain phones numbers and only capture those VOIP conversations. I would typically have between 1-3 phone numbers being monitored.</p><p>As I have it now, I am catching every phone call made on the system. I am confident that as I add the monitoring to more servers space will become an issue. I do have a ring buffer setup for 100 files that are 100 megs each.</p></div><div id="comment-3817-info" class="comment-info"><span class="comment-age">(29 Apr '11, 11:58)</span> Travis Young</div></div><span id="3818"></span><div id="comment-3818" class="comment"><div id="post-3818-score" class="comment-score">1</div><div class="comment-text"><p>It would help if you told us the capture filter(s) you're currently using and even more helpful would be a sample pcap. Help us help you! :)</p></div><div id="comment-3818-info" class="comment-info"><span class="comment-age">(29 Apr '11, 12:03)</span> bstn</div></div><span id="3819"></span><div id="comment-3819" class="comment"><div id="post-3819-score" class="comment-score"></div><div class="comment-text"><p>I am currently using currently using "host xxx.xxx.xxx.xxx", which is the IP of voice gateway, as my capture filter.</p></div><div id="comment-3819-info" class="comment-info"><span class="comment-age">(29 Apr '11, 12:19)</span> Travis Young</div></div></div><div id="comment-tools-3800" class="comment-tools"></div><div class="clear"></div><div id="comment-3800-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3838"></span>

<div id="answer-container-3838" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3838-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds like you're looking for a <a href="http://ask.wireshark.org/questions/3166/voip-call-recording">Call Recorder</a>, something Wireshark is not.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '11, 02:06</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-3838" class="comments-container"><span id="3917"></span><div id="comment-3917" class="comment"><div id="post-3917-score" class="comment-score">1</div><div class="comment-text"><p>While I am looking to record calls, I also need the ability to to see the full process of the call starting/ending. As we need to dissect a call and see if the issue is on my companies side or the phone companies side.</p><p>We normally use Wireshark to monitor various customers as issues arises, and common tasks are as follows:</p><p>1: If the phone company has been stripping out the DTMF tones.</p><p>2: To see when/if/why/how our application is starting its automated recording before a customer has answered their phone.</p><p>3: To monitor calls so we can see if our application or the phone company is hanging up on customers.</p><p>If we can streamline the process and make it a faster process, that would be great. As it stands, we spend about a half hour per person (per customer) each day. If what I need is a call recorder. I would need it:</p><p>1: To capture all of the packets for each call</p><p>2: Display dual channels so I can visually see the call while listening to it,</p><p>3: Show me a graph of the call so that I can see where the call was initiated and ended.</p><p>Any recommendations?</p></div><div id="comment-3917-info" class="comment-info"><span class="comment-age">(04 May '11, 06:28)</span> Travis Young</div></div></div><div id="comment-tools-3838" class="comment-tools"></div><div class="clear"></div><div id="comment-3838-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3930"></span>

<div id="answer-container-3930" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3930-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Check this out <a href="http://wiki.wireshark.org/Lua/Examples">http://wiki.wireshark.org/Lua/Examples</a></p><p>section: Dump VoIP calls into separate files</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 May '11, 19:23</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p>izopizo<br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 May '11, 19:24</p></div></div><div id="comments-container-3930" class="comments-container"><span id="3936"></span><div id="comment-3936" class="comment"><div id="post-3936-score" class="comment-score"></div><div class="comment-text"><p>I noticed that the script calls for a MYSQL DB. Does it really need it? Each of our machines resources are closely regulated, so adding the mysql client would be an issue.</p></div><div id="comment-3936-info" class="comment-info"><span class="comment-age">(05 May '11, 05:54)</span> Travis Young</div></div><span id="3940"></span><div id="comment-3940" class="comment"><div id="post-3940-score" class="comment-score"></div><div class="comment-text"><p>@Travis, It doesn't need to be MySQL, but the script does rely on some kind of DB. The <a href="http://www.keplerproject.org/luasql/manual.html">LuaSQL</a> library supports several different DBs (including SQLite). If you can't have this dependency, then an alternative might be to replace those DB calls with Lua functions. Also note that this script assumes the OS is *nix (based on the <code>mkdir -p</code>), so if you're in Windows, you'd have to put Cygwin in your path for the script to work properly.</p></div><div id="comment-3940-info" class="comment-info"><span class="comment-age">(05 May '11, 07:37)</span> bstn</div></div></div><div id="comment-tools-3930" class="comment-tools"></div><div class="clear"></div><div id="comment-3930-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

