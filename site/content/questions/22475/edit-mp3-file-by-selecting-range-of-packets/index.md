+++
type = "question"
title = "Edit MP3 file by selecting range of packets"
description = '''I&#x27;ve captured streaming audio into a trace file, and I can isolate the conversation and save it as an MP3 with no problem and it works great! Once I&#x27;ve saved the MP3 file, I listen to it with Audacity and make a note of some time blocks I&#x27;d like to remove. What I&#x27;d like to do is be able to surgicall...'''
date = "2013-06-29T16:22:00Z"
lastmod = "2013-06-29T19:40:00Z"
weight = 22475
keywords = [ "edit", "tracefile", "mp3" ]
aliases = [ "/questions/22475" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Edit MP3 file by selecting range of packets](/questions/22475/edit-mp3-file-by-selecting-range-of-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22475-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22475-score" class="post-score" title="current number of votes">0</div><span id="post-22475-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've captured streaming audio into a trace file, and I can isolate the conversation and save it as an MP3 with no problem and it works great!</p><p>Once I've saved the MP3 file, I listen to it with Audacity and make a note of some time blocks I'd like to remove. What I'd like to do is be able to surgically select a range of packets (which, in this case, are the commercials) and delete them from the trace file and then re-save all of the packets as a new MP3 file (minus the commercials or any other junk I don't want as part of my final MP3 file).</p><p>Surely there's a way to select a range (ideally, multiple ranges) of packets and delete then from your trace file, isn't there?</p><p>Thank you, Ed</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-edit" rel="tag" title="see questions tagged &#39;edit&#39;">edit</span> <span class="post-tag tag-link-tracefile" rel="tag" title="see questions tagged &#39;tracefile&#39;">tracefile</span> <span class="post-tag tag-link-mp3" rel="tag" title="see questions tagged &#39;mp3&#39;">mp3</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jun '13, 16:22</strong></p><img src="https://secure.gravatar.com/avatar/7084909dd8e357d1ef16d4dce0d4fdb4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ed_Flecko&#39;s gravatar image" /><p><span>Ed_Flecko</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ed_Flecko has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Jun '13, 17:23</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-22475" class="comments-container"></div><div id="comment-tools-22475" class="comment-tools"></div><div class="clear"></div><div id="comment-22475-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22476"></span>

<div id="answer-container-22476" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22476-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22476-score" class="post-score" title="current number of votes">1</div><span id="post-22476-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, you could do that by applying filters like "frame.number &lt; x or frame.number &gt; y", with x being the beginning of the frames you want to remove and y being the end. With that filter you'll keep the other packets visible, which you can then export using "File" -&gt; "Export Specified Packets" -&gt; "All Packets - Displayed". Then reload the new file.</p><p>BUT - it makes no sense. Removing the packets will result in a damaged MP3 file because parts are missing from it that aren't surgically removed from a MP3 file format point of view.</p><p>AND - why don't you use Audacity instead - it is a audio editor with which you can easily remove the parts you don't like. Doing it to the trace makes absolutely no sense in my opinion. It's like using a chainsaw on a cow when all you want to do is cut a single steak from a larger piece of filet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '13, 18:40</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Jun '13, 18:41</strong> </span></p></div></div><div id="comments-container-22476" class="comments-container"><span id="22477"></span><div id="comment-22477" class="comment"><div id="post-22477-score" class="comment-score"></div><div class="comment-text"><p>Jasper, The main reason why I don't use Audacity to do the editing is because what starts as an approximately 15Mb file from Wireshark becomes a 75Mb as soon as you wash it through Audacity!</p><p>And you may be right - editing it with Wireshark may result in an unusable MP3 file but that's exactly what I want to find out - CAN it be successfully "edited" with Wireshark and keep the dramatically smaller file size?...or do I simply HAVE to use an audio editing program?</p><p>Ed</p></div><div id="comment-22477-info" class="comment-info"><span class="comment-age">(29 Jun '13, 19:36)</span> <span class="comment-user userinfo">Ed_Flecko</span></div></div><span id="22478"></span><div id="comment-22478" class="comment"><div id="post-22478-score" class="comment-score"></div><div class="comment-text"><p>I'd say you have to use an audio editing program. And the size is getting bigger if you write the file as uncompressed WAVE or when using MP3 compression that isn't as high as the original. You should try to find out what bit rate the file was compressed with originally and write the cleaned file with the same ratio. Or try a cutting program that doesn't recode, like this one: <a href="http://mpesch3.de1.cc/mp3dc.html">http://mpesch3.de1.cc/mp3dc.html</a></p></div><div id="comment-22478-info" class="comment-info"><span class="comment-age">(29 Jun '13, 19:40)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-22476" class="comment-tools"></div><div class="clear"></div><div id="comment-22476-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

