+++
type = "question"
title = "How to extract IP addresses from .cap file to text file?"
description = '''At my work we have a computer running Dumpcap to capture LAN traffic into hourly captures. What is the easiest way via command line and with what tool to extract a list of IP addresses from the .cap files(post capture) and output them to a text file. Looking to output all Destination and Source IP a...'''
date = "2014-11-22T16:52:00Z"
lastmod = "2014-12-13T21:21:00Z"
weight = 38071
keywords = [ "ip", "text", "extract", "command-line", "output" ]
aliases = [ "/questions/38071" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to extract IP addresses from .cap file to text file?](/questions/38071/how-to-extract-ip-addresses-from-cap-file-to-text-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38071-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38071-score" class="post-score" title="current number of votes">0</div><span id="post-38071-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>At my work we have a computer running Dumpcap to capture LAN traffic into hourly captures. What is the easiest way via command line and with what tool to extract a list of IP addresses from the .cap files(post capture) and output them to a text file. Looking to output all Destination and Source IP addresses, and if possible filter out all local 192.168.x.x. traffic IP's. Hoping to have a single IP per line in the text file. Any help would be much appreciated, thanks.</p><p>Maybe this is possible: tshark -r input.cap -w output.txt -R "Some type of filter here"</p><p>Our use case: We are hoping to compare this output text file of IP addresses to a list of IP from various malware resource groups who post IP's associated with the most current C&amp;C servers and malware hoping to alert us of an infection by one of our users via email upon a match. It will be ran via a batch file hence the command line method hourly after an hourly capture has been completed.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-text" rel="tag" title="see questions tagged &#39;text&#39;">text</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-command-line" rel="tag" title="see questions tagged &#39;command-line&#39;">command-line</span> <span class="post-tag tag-link-output" rel="tag" title="see questions tagged &#39;output&#39;">output</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Nov '14, 16:52</strong></p><img src="https://secure.gravatar.com/avatar/7c34b5795df1aaa486754544342bfc1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zer0day&#39;s gravatar image" /><p><span>zer0day</span><br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zer0day has 3 accepted answers">60%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Nov '14, 17:11</strong> </span></p></div></div><div id="comments-container-38071" class="comments-container"></div><div id="comment-tools-38071" class="comment-tools"></div><div class="clear"></div><div id="comment-38071-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="38550"></span>

<div id="answer-container-38550" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38550-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38550-score" class="post-score" title="current number of votes">0</div><span id="post-38550-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="zer0day has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have found my answer after many hours of trial and error....</p><p>To get destination and source IP addresses from a capture using tshark I used the command below:</p><pre><code>`tshark -r &lt;input file&gt; -T fields -e ip.dst -e ip.src &gt; path\output.txt`</code></pre><p>So, after figuring this out I incorporated this into a powershell script to sort, get unique list of destination IP addresses(decided to only use destination -e ip.dst), and to filter out any 192.168.x.x traffic IP's. Here is my powershell script...</p><pre><code>gci C:\Users\User\Desktop\capturetest\*.cap | where {!$_.PSIsContainer} | sort LastWriteTime | select -f 1 | move -destination &quot;C:\Users\User\Desktop\target1&quot;

gci C:\Users\User\Desktop\target1 *.cap | rename-item -newname capture.cap

tshark -r C:\Users\User\Desktop\target1\capture.cap -T fields -e ip.dst &gt; C:\Users\User\Desktop\target1\ip.txt

gc C:\Users\User\Desktop\target1\ip.txt | sort | get-unique | select-string -pattern &quot;192.168&quot; -notmatch | Out-File C:\Users\User\Desktop\target1\match.txt

gci C:\Users\User\Desktop\target1\match.txt | move -destination &quot;\\192.168.1.4\folder\outbound&quot;

Remove-Item C:\Users\User\Desktop\target1\ip.txt

Remove-Item C:\Users\User\Desktop\target1\capture.cap</code></pre><p>A run through:</p><p>I have dumpcap running doing a round robin of two one hour captures in a folder labeled "capturetest", script looks in the folder for a file with the .cap extension, finds a .cap file with the last write time and moves it to a folder called, "target1".</p><pre><code>gci C:\Users\User\Desktop\capturetest\*.cap | where {!$_.PSIsContainer} | sort LastWriteTime | select -f 1 | move -destination &quot;C:\Users\User\Desktop\target1&quot;</code></pre><p>Then once moved to target1 the cap file get renamed to "capture.cap"</p><pre><code>gci C:\Users\User\Desktop\target1 *.cap | rename-item -newname capture.cap</code></pre><p>Then tshark does it thing to export out destination IP addresses to a text file called, "ip.txt"</p><pre><code>tshark -r C:\Users\User\Desktop\target1\capture.cap -T fields -e ip.dst &gt; C:\Users\User\Desktop\target1\ip.txt</code></pre><p>Now that we have a list of destination IP's we need to get rid of duplicates IP's and filter out any 192.168.x.x traffic. This will be output to "match.txt"</p><pre><code>gc C:\Users\User\Desktop\target1\ip.txt | sort | get-unique | select-string -pattern &quot;192.168&quot; -notmatch | Out-File C:\Users\User\Desktop\target1\match.txt</code></pre><p>Now the match.txt file gets moved to a server share where another script compares match.txt to another text file which is a blacklist compiled from various different sources of malicious and compromised IP's.</p><pre><code>gci C:\Users\User\Desktop\target1\match.txt | move -destination &quot;\\192.168.1.4\folder\outbound&quot;</code></pre><p>Then Since I have this powershell script running as a scheduled task hourly we need to do some cleanup just to be tidy.</p><pre><code>Remove-Item C:\Users\User\Desktop\target1\ip.txt

Remove-Item C:\Users\User\Desktop\target1\capture.cap</code></pre><p>Edit: To run tshark as it is scripted, you will need to add tshark's path to your environment variables. This script is running on Window 7 Pro with Powershell v2. Here's a how to: <a href="http://www.computerhope.com/issues/ch000549.htm">http://www.computerhope.com/issues/ch000549.htm</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Dec '14, 21:21</strong></p><img src="https://secure.gravatar.com/avatar/7c34b5795df1aaa486754544342bfc1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zer0day&#39;s gravatar image" /><p><span>zer0day</span><br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zer0day has 3 accepted answers">60%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Aug '17, 18:23</strong> </span></p></div></div><div id="comments-container-38550" class="comments-container"></div><div id="comment-tools-38550" class="comment-tools"></div><div class="clear"></div><div id="comment-38550-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38074"></span>

<div id="answer-container-38074" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38074-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38074-score" class="post-score" title="current number of votes">2</div><span id="post-38074-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Maybe this is possible: tshark -r input.cap -w output.txt -R "Some type of filter here"</p></blockquote><p>It's possible, but it won't do what you want - all a filter does is control which packets to process; it doesn't affect the format of the output. Furthermore, <code>-w</code> writes out a capture file, not arbitrary text.</p><p>It's not the most convenient, but you could try doing</p><pre><code>tshark -q -r input.cap -z ip_hosts,tree</code></pre><p>That will print out, to the standard output, a list of all source and destination IP addresses in the file, along with some statistics about the traffic to and from each of the hosts. If you just want a list of addresses, you'll have to run it through another program to filter out all the headers, etc.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '14, 00:15</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Nov '14, 00:16</strong> </span></p></div></div><div id="comments-container-38074" class="comments-container"></div><div id="comment-tools-38074" class="comment-tools"></div><div class="clear"></div><div id="comment-38074-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

