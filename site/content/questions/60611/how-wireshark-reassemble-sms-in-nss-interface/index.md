+++
type = "question"
title = "how Wireshark reassemble SMS in NSS interface?"
description = '''Hi all I&#x27;m working on the gsm signaling data and now I have an data that related to NSS interface (I mean this data has the hierarchy like this --&amp;gt; MTP2, MTP3, SCCP, TCAP , MAP and SMS) In some of SMS data I have an SMS which has TPU-header and this section show that this SMS has another parts. I...'''
date = "2017-04-06T04:24:00Z"
lastmod = "2017-04-06T04:24:00Z"
weight = 60611
keywords = [ "gsm_sms", "nosm-rp-oa", "sms", "reassemble", "nosm-rp-da" ]
aliases = [ "/questions/60611" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how Wireshark reassemble SMS in NSS interface?](/questions/60611/how-wireshark-reassemble-sms-in-nss-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60611-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60611-score" class="post-score" title="current number of votes">1</div><span id="post-60611-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all</p><p>I'm working on the gsm signaling data and now I have an data that related to NSS interface (I mean this data has the hierarchy like this --&gt; MTP2, MTP3, SCCP, TCAP , MAP and SMS)</p><p>In some of SMS data I have an SMS which has TPU-header and this section show that this SMS has another parts. In the TCAP which we have RP information and by using them and the header we can concatenating SMSs. But in the TCAP we don't have any information about RP-OA and RP-DA--I mean both of them are nosm-RP-OA and nosm-RP-DA! So how should reassembles them? I think Wireshark in this interface has some bugs! Since I have some packets that TP-OA address are not same but Wireshark reassemble them! Is there any one experienced this problem and how solve it?</p><p>thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gsm_sms" rel="tag" title="see questions tagged &#39;gsm_sms&#39;">gsm_sms</span> <span class="post-tag tag-link-nosm-rp-oa" rel="tag" title="see questions tagged &#39;nosm-rp-oa&#39;">nosm-rp-oa</span> <span class="post-tag tag-link-sms" rel="tag" title="see questions tagged &#39;sms&#39;">sms</span> <span class="post-tag tag-link-reassemble" rel="tag" title="see questions tagged &#39;reassemble&#39;">reassemble</span> <span class="post-tag tag-link-nosm-rp-da" rel="tag" title="see questions tagged &#39;nosm-rp-da&#39;">nosm-rp-da</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Apr '17, 04:24</strong></p><img src="https://secure.gravatar.com/avatar/5ba805384013fecf04be3762b8cb1421?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shafagh&#39;s gravatar image" /><p><span>Shafagh</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shafagh has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Apr '17, 06:05</strong> </span></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-60611" class="comments-container"></div><div id="comment-tools-60611" class="comment-tools"></div><div class="clear"></div><div id="comment-60611-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

