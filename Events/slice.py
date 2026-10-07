import pygame

def nine_slice(image, width, height, border=20):
    result = pygame.Surface((width, height), pygame.SRCALPHA)

    src_w, src_h = image.get_size()

    # 四个角
    top_left = image.subsurface((0, 0, border, border))
    top_right = image.subsurface(
        (src_w - border, 0, border, border)
    )
    bottom_left = image.subsurface(
        (0, src_h - border, border, border)
    )
    bottom_right = image.subsurface(
        (src_w - border, src_h - border, border, border)
    )

    # 四条边
    top = image.subsurface(
        (border, 0, src_w - 2 * border, border)
    )
    bottom = image.subsurface(
        (border, src_h - border, src_w - 2 * border, border)
    )
    left = image.subsurface(
        (0, border, border, src_h - 2 * border)
    )
    right = image.subsurface(
        (src_w - border, border, border, src_h - 2 * border)
    )

    # 中间
    center = image.subsurface(
        (border, border,
         src_w - 2 * border,
         src_h - 2 * border)
    )

    # 目标尺寸
    middle_w = width - 2 * border
    middle_h = height - 2 * border

    # 四个角 —— 原尺寸，完全不变
    result.blit(top_left, (0, 0))
    result.blit(top_right, (width - border, 0))
    result.blit(bottom_left, (0, height - border))
    result.blit(bottom_right, (width - border, height - border))

    # 上下边 —— 只横向拉伸
    top_scaled = pygame.transform.scale(top, (middle_w, border))
    bottom_scaled = pygame.transform.scale(bottom, (middle_w, border))

    result.blit(top_scaled, (border, 0))
    result.blit(bottom_scaled, (border, height - border))

    # 左右边 —— 只纵向拉伸
    left_scaled = pygame.transform.scale(left, (border, middle_h))
    right_scaled = pygame.transform.scale(right, (border, middle_h))

    result.blit(left_scaled, (0, border))
    result.blit(right_scaled, (width - border, border))

    # 中间 —— 横纵都拉伸
    center_scaled = pygame.transform.scale(
        center,
        (middle_w, middle_h)
    )

    result.blit(center_scaled, (border, border))

    return result