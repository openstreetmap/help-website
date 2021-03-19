+++
type = "question"
title = "Decode USB Interface Class correctly"
description = '''Hi! I am using Wireshark 1.12.7 on vivid and I captured a few hours of mouse movements and keyboard interrupts. One thing that really bothers me, is the wrong decoding of the value bInterfaceClass. For some reason it never gets decoded properly (always bInterfaceClass: Unknown (0xffff)). For compari...'''
date = "2015-09-18T04:26:00Z"
lastmod = "2015-09-18T14:02:00Z"
weight = 45944
keywords = [ "usb", "usbmon", "wireshark" ]
aliases = [ "/questions/45944" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Decode USB Interface Class correctly](/questions/45944/decode-usb-interface-class-correctly)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45944-score" class="post-score" title="current number of votes">0</div><span id="post-45944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi!</p><p>I am using Wireshark 1.12.7 on vivid and I captured a few hours of mouse movements and keyboard interrupts. One thing that really bothers me, is the wrong decoding of the value <code>bInterfaceClass</code>.<br />
For some reason it never gets decoded properly (always <code>bInterfaceClass: Unknown (0xffff)</code>). For comparison I used <code>sudo lsusb -v</code> which results in:</p><pre><code>Device Descriptor:
  bLength                18
  bDescriptorType         1
  bcdUSB               1.10
  bDeviceClass            0 (Defined at Interface level)
  bDeviceSubClass         0 
  bDeviceProtocol         0 
  bMaxPacketSize0         8
  idVendor           0x04b3 IBM Corp.
  idProduct          0x3025 NetVista Full Width Keyboard
  bcdDevice            1.02
  iManufacturer           1 CHICONY
  iProduct                2 USB NetVista Full Width Keyboard
  iSerial                 0 
  bNumConfigurations      1
  Configuration Descriptor:
    bLength                 9
    bDescriptorType         2
    wTotalLength           34
    bNumInterfaces          1
    bConfigurationValue     1
    iConfiguration          0 
    bmAttributes         0xa0
      (Bus Powered)
      Remote Wakeup
    MaxPower              100mA
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        0
      bAlternateSetting       0
      bNumEndpoints           1
      bInterfaceClass         3 Human Interface Device
      bInterfaceSubClass      1 Boot Interface Subclass
      bInterfaceProtocol      1 Keyboard
      iInterface              0 
        HID Device Descriptor:
[...]</code></pre><p>So it would actually have a "correct" class.</p><p>Is there anything I can do to make wireshark decode the interface class correctly?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-usb" rel="tag" title="see questions tagged &#39;usb&#39;">usb</span> <span class="post-tag tag-link-usbmon" rel="tag" title="see questions tagged &#39;usbmon&#39;">usbmon</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Sep '15, 04:26</strong></p><img src="https://secure.gravatar.com/avatar/ed42d94d476f543682fea8aab051d515?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rolf&#39;s gravatar image" /><p><span>Rolf</span><br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rolf has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-45944" class="comments-container"></div><div id="comment-tools-45944" class="comment-tools"></div><div class="clear"></div><div id="comment-45944-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45951"></span>

<div id="answer-container-45951" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45951-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45951-score" class="post-score" title="current number of votes">1</div><span id="post-45951-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Rolf has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To get usb.bInterfaceClass displaying the real value (and not 0xffff) you need to capture the USB enumeration procedure (as seen in this <a href="https://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=Bluetooth_HCI_and_OBEX_Transaction_over_USB.ntar.gz">capture</a> from Wiresahrk wiki for example).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Sep '15, 11:09</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-45951" class="comments-container"><span id="45954"></span><div id="comment-45954" class="comment"><div id="post-45954-score" class="comment-score"></div><div class="comment-text"><p>This was the problem :) thanks a lot!</p></div><div id="comment-45954-info" class="comment-info"><span class="comment-age">(18 Sep '15, 14:02)</span> <span class="comment-user userinfo">Rolf</span></div></div></div><div id="comment-tools-45951" class="comment-tools"></div><div class="clear"></div><div id="comment-45951-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

