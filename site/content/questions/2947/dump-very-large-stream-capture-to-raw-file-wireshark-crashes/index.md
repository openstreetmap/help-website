+++
type = "question"
title = "Dump very large stream capture to raw file (Wireshark crashes)"
description = '''Hello, I&#x27;m trying to dump a very large tcp stream (600 MB) in raw format.  I captured the stream and saved it to disk. Then I open it again and I want to open the &quot;Follow TCP Stream&quot; window to be able to save the stream (only the downwards direction) in raw format to my disk. So I click on &quot;Follow T...'''
date = "2011-03-20T10:01:00Z"
lastmod = "2011-03-21T16:03:00Z"
weight = 2947
keywords = [ "large", "raw", "stream", "dump", "follow" ]
aliases = [ "/questions/2947" ]
osqa_answers = 5
osqa_accepted = false
+++

<div class="headNormal">

# [Dump very large stream capture to raw file (Wireshark crashes)](/questions/2947/dump-very-large-stream-capture-to-raw-file-wireshark-crashes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2947-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2947-score" class="post-score" title="current number of votes">1</div><span id="post-2947-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm trying to dump a very large tcp stream (600 MB) in raw format. I captured the stream and saved it to disk. Then I open it again and I want to open the "Follow TCP Stream" window to be able to save the stream (only the downwards direction) in raw format to my disk. So I click on "Follow TCP Stream", Filtering works fine but as soon as the Progress bar reaches 99%, memory consumption rises excessively until Wireshark crashes. As it only crashes after the filtering is almost complete, I imagine this is a problem with the GUI. (Loading 600 MB into the GUI might be very memory consuming).</p><p>So my question is: Is there a way to circumvent this crash? Is it maybe possible to dump the onedirectional raw stream directly into a file without using the "Follow TCP stream" window in the GUI? I checked command line options but I couln't find an appropriate function there.</p><p>I would appreaciate any help on that.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-large" rel="tag" title="see questions tagged &#39;large&#39;">large</span> <span class="post-tag tag-link-raw" rel="tag" title="see questions tagged &#39;raw&#39;">raw</span> <span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span> <span class="post-tag tag-link-dump" rel="tag" title="see questions tagged &#39;dump&#39;">dump</span> <span class="post-tag tag-link-follow" rel="tag" title="see questions tagged &#39;follow&#39;">follow</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Mar '11, 10:01</strong></p><img src="https://secure.gravatar.com/avatar/e17759ffaa3754292631d22ceb4344d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Welch13&#39;s gravatar image" /><p><span>Welch13</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Welch13 has no accepted answers">0%</span></p></div></div><div id="comments-container-2947" class="comments-container"></div><div id="comment-tools-2947" class="comment-tools"></div><div class="clear"></div><div id="comment-2947-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

5 Answers:

</div>

</div>

<span id="2950"></span>

<div id="answer-container-2950" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2950-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2950-score" class="post-score" title="current number of votes">1</div><span id="post-2950-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can circumvent memory usage related crashes by cutting your very large trace file into smaller files using the command line tool "editcap" which is installed together with Wireshark. I usually use the "-c" parameter to cut my files into pieces of 100,000 frames each. Wireshark should have no problem with loading these.</p><p>Problem is, as soon as you cut your large file into pieces you probably won't like it because the stream you're trying to extract is spanning multiple files. For that kind of problem I usually create a batch file that calls another command line tool, "tshark", on each of them and use the parameters</p><p><code>-r &lt;infile&gt; -R "filter to extract the TCP flow by socket paramters" -w &lt;outfile&gt;</code>.</p><p>Afterwards, I use the third command line tool <code>mergecap -a</code> to concatenate the extracted pieces of the flow, which usually is a lot smaller than the large file I started with.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '11, 12:52</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-2950" class="comments-container"></div><div id="comment-tools-2950" class="comment-tools"></div><div class="clear"></div><div id="comment-2950-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2952"></span>

<div id="answer-container-2952" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2952-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2952-score" class="post-score" title="current number of votes">0</div><span id="post-2952-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks for your answer, but does mergecap work on raw (binary) files ?? If so, how would I invoke that option?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '11, 13:09</strong></p><img src="https://secure.gravatar.com/avatar/e17759ffaa3754292631d22ceb4344d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Welch13&#39;s gravatar image" /><p><span>Welch13</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Welch13 has no accepted answers">0%</span></p></div></div><div id="comments-container-2952" class="comments-container"></div><div id="comment-tools-2952" class="comment-tools"></div><div class="clear"></div><div id="comment-2952-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2955"></span>

<div id="answer-container-2955" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2955-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2955-score" class="post-score" title="current number of votes">0</div><span id="post-2955-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I guess by "raw" you mean it's binary, usually in pcap format - mergecap works on the same binary trace file formats like Wireshark. You can concatenate files like this:</p><p><code>mergecap -a -w &lt;outfile&gt; &lt;infile1&gt; &lt;infile2&gt; &lt;infile&gt;...&lt;infile#&gt;</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '11, 15:03</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-2955" class="comments-container"></div><div id="comment-tools-2955" class="comment-tools"></div><div class="clear"></div><div id="comment-2955-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2967"></span>

<div id="answer-container-2967" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2967-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2967-score" class="post-score" title="current number of votes">0</div><span id="post-2967-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Is all that 600MB of data really needed, i.e., all of it is part of the stream of interest? If not, you might try using as stringent a capture filter as possible to limit the number of packets you capture to begin with. If you already have a large capture file with lots of extraneous packets, you might try using tshark instead of Wireshark to do your filtering.</p><p>For more information on "Out of Memory" issues, see <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">http://wiki.wireshark.org/KnownBugs/OutOfMemory</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '11, 07:43</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-2967" class="comments-container"></div><div id="comment-tools-2967" class="comment-tools"></div><div class="clear"></div><div id="comment-2967-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2978"></span>

<div id="answer-container-2978" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2978-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2978-score" class="post-score" title="current number of votes">0</div><span id="post-2978-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, almost all of the 600 MB is actually needed. To clearify that: The capture file of interest is already filtered. It contains all the up- and downstream information from one single connection from one single IP in the network to one single IP on one port during 2 hours; I imagine the user watched some kind of flash video of a church service. And I want to reconstruct the downstream part of it. So filtering really isn't the issue. It's rather to extract the downstream part (upstream might only be 5% of the filesize) and write it into a binary file which can be used to reconstruct the full stream the application on the users computer saw at the time.</p><p>I'm still trying to get the proposed solution from Jasper working. In the meantime further comments and solutions are of course welcome.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '11, 13:23</strong></p><img src="https://secure.gravatar.com/avatar/e17759ffaa3754292631d22ceb4344d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Welch13&#39;s gravatar image" /><p><span>Welch13</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Welch13 has no accepted answers">0%</span></p></div></div><div id="comments-container-2978" class="comments-container"><span id="2989"></span><div id="comment-2989" class="comment"><div id="post-2989-score" class="comment-score"></div><div class="comment-text"><p>Well if your 600 MB file is already filtered to the one stream you want to extract my method won't help much - I was under the assumption that it contained irrelelevant data as well.</p><p>Maybe the cutting process with editcap can help to extract the payload of smaller trace files using the "Follow TCP stream" option and then it might be possible to concatenate the extracted content with "copy &lt;contentfile1&gt; /b + &lt;contentfile2&gt; /b + ... &lt;contentfile#&gt; &lt;destinationfile&gt; /b" (binary copy of files)</p></div><div id="comment-2989-info" class="comment-info"><span class="comment-age">(21 Mar '11, 16:03)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-2978" class="comment-tools"></div><div class="clear"></div><div id="comment-2978-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

