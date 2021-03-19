+++
type = "question"
title = "Sanitising NTLM Tokens"
description = '''Hallo. I am trying to find a way to sanitise Information contained in NTLMSSP embedded(Yes I know I can remove everything from level 4 up, but that doesn&#x27;t help when I am looking at an Authentication problem in a web page) I have openened the packet in an editor.  I have found the token and decoded ...'''
date = "2015-07-24T23:13:00Z"
lastmod = "2015-07-26T12:32:00Z"
weight = 44464
keywords = [ "sanitize" ]
aliases = [ "/questions/44464" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Sanitising NTLM Tokens](/questions/44464/sanitising-ntlm-tokens)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44464-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44464-score" class="post-score" title="current number of votes">0</div><span id="post-44464-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hallo.</p><p>I am trying to find a way to sanitise Information contained in NTLMSSP embedded(Yes I know I can remove everything from level 4 up, but that doesn't help when I am looking at an Authentication problem in a web page) I have openened the packet in an editor.</p><p>I have found the token and decoded from base64, I have replaced the offending strings. I have then reencoded to Base64 and replaced the Binary data. I have set the length of the Packet (I think) but I cannot get it to open after editing it.</p><p>Is there a way to actually do this? Strings I can replace, Hex even, but as soon as I change the Base64 (yes the whole encode) the packet and capture are dead.. I am suddenly finding a lot of respect for TraceWrangler + Bittwiste.</p><p>My HOPE was to change the file manually, run it through TraceWrangler to recalculate the CRCs and have a good time afterall. Any Ideas where I am going wrong or if I can actually go right?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sanitize" rel="tag" title="see questions tagged &#39;sanitize&#39;">sanitize</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jul '15, 23:13</strong></p><img src="https://secure.gravatar.com/avatar/05ba95262a3352e3af4ba69c0ec0dff2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DarrenWright&#39;s gravatar image" /><p><span>DarrenWright</span><br />
<span class="score" title="216 reputation points">216</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DarrenWright has 5 accepted answers">26%</span></p></div></div><div id="comments-container-44464" class="comments-container"></div><div id="comment-tools-44464" class="comment-tools"></div><div class="clear"></div><div id="comment-44464-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44473"></span>

<div id="answer-container-44473" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44473-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44473-score" class="post-score" title="current number of votes">0</div><span id="post-44473-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="DarrenWright has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have you tried replacing the base64 encode parts with the new base64 encodings using the string replacement feature of TraceWrangler? Only requirement is to keep the string length identical, but it should work.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jul '15, 08:19</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-44473" class="comments-container"><span id="44476"></span><div id="comment-44476" class="comment"><div id="post-44476-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper, I was playing with it until around 3 this morning (we finally got rain so I stayed up and enjoyed it..) I was going to try later on again. I have the feeling my last 90 minutes were a little too Whisky laden and not very productive :(</p><p>Just out of curiosity, I would need to re encode the strings and search for the old ones to replace in Hex or Binary? I tried just searching on Hex, that didn't work yet.</p><p>The problem sa I see it is a Base 64 of one 10 letter word wont be the same length as a Base64 of another 10 letter word. If I replace the STRING in a decoded Base64 and reencode it, it is never going to be the same length as the one I am replacing. And just to annoy me further the NTLMSSP seem to be a abse64 encode of the whole token at once. Even harder to match, and if I pad or remove, then the dissector wont be able to recognize it.. Or I just really am doing something worng.. which at this point would probably make me happier than the alternatives..</p></div><div id="comment-44476-info" class="comment-info"><span class="comment-age">(25 Jul '15, 09:14)</span> <span class="comment-user userinfo">DarrenWright</span></div></div><span id="44489"></span><div id="comment-44489" class="comment"><div id="post-44489-score" class="comment-score"></div><div class="comment-text"><p>You can search in Hex if you put the values between pipe symbols, similar to how Snort patterns work. E.g. if you search for <strong>0x12ab</strong> you'd use <strong>|12 ab|</strong></p><p>Problem with the length is that if you replace something with more or less bytes all sequence numbers of the following packets are incorrect and the TCP expert will go crazy, so right now I don't allow it. I'll have to deal with that in the future though when I start working on sanitization of protocols on top of TCP.</p><p>I need to find a packet with NTLMSSP to see how it looks like; maybe I can do something to make things easier for you somehow.</p><p>Also, I wonder why same length strings end up in different length Base64 encodings for you - in my tests that never happened.</p></div><div id="comment-44489-info" class="comment-info"><span class="comment-age">(25 Jul '15, 15:18)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="44493"></span><div id="comment-44493" class="comment"><div id="post-44493-score" class="comment-score"></div><div class="comment-text"><p>Hmm. I tested this about 50 times today and I didn't manage to get a different length string (That was probably the whisky..)</p><p>I am back at work tomorrow, I will test this again with the snort type search. For the sake of splitting hairs:</p><ol><li>manually find the hex representation of the Token</li><li>decode the whole thing</li><li>swap out the offending string</li><li>recode to Base64</li><li>Search for the original token in hex and replace it with the new token also in hex using tracewrangler</li></ol><p>Is this correct? You're definately earning a coffee here :)</p></div><div id="comment-44493-info" class="comment-info"><span class="comment-age">(26 Jul '15, 03:57)</span> <span class="comment-user userinfo">DarrenWright</span></div></div><span id="44494"></span><div id="comment-44494" class="comment"><div id="post-44494-score" class="comment-score"></div><div class="comment-text"><p>Yeah, let's blame the Whisky (not that Whisky is a bad thing, cheers! :-))</p><p>And your steps sound about right; it's what I'd do to see if it gets me the correct results. If it doesn't work let me know; the content replacement in the payloads may still have some bugs.</p></div><div id="comment-44494-info" class="comment-info"><span class="comment-age">(26 Jul '15, 04:17)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="44507"></span><div id="comment-44507" class="comment"><div id="post-44507-score" class="comment-score"></div><div class="comment-text"><p>I'm gonna mark this as answered, if it doesn't ACTUALLY work, I'll send you a Bug + pcap + steps taken via Mail, may help you in Bug tracking at some point.</p></div><div id="comment-44507-info" class="comment-info"><span class="comment-age">(26 Jul '15, 12:30)</span> <span class="comment-user userinfo">DarrenWright</span></div></div><span id="44508"></span><div id="comment-44508" class="comment not_top_scorer"><div id="post-44508-score" class="comment-score"></div><div class="comment-text"><p>hm, okay, thanks, I'll take a look as soon as I can to see what I can do and where the problem is.</p></div><div id="comment-44508-info" class="comment-info"><span class="comment-age">(26 Jul '15, 12:32)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-44473" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-44473-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

